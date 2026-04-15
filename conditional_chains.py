from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1 = ChatOpenAI()

model2 = ChatGroq(model_name="llama-3.3-70b-versatile")

parse = StrOutputParser()

class Feedback(BaseModel):
    sentiments: Literal['positive', 'negative'] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model1 | parser2

prompt2 = PromptTemplate(
    template = 'Write a appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write a appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiments =='positive' , prompt2 | model1 | parse),
    (lambda x:x.sentiments == 'negative' , prompt3 | model1 | parse),
    RunnableLambda(lambda x: 'Could not classify the sentiment')
)

chain = classifier_chain | branch_chain

# print(chain.invoke({ "feedback": 'The product quality is really bad and I am not happy with the purchase' }))

chain.get_graph().print_ascii()


