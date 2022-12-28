import os
import openai
import config

OPENAI_API_KEY= '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'
openai.api_key = config.OPENAI_API_KEY
def generateBlogTopics(prompt1):
 response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Generate blog topics on: {}.".format(prompt1),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
 )
 return response ['choices'][0]['text']

def generateBlogSection(prompt2):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Expand blog  topic into high level blog section:{}. \n \n".format(prompt2),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
 )
  return response ['choices'][0]['text']


def BlogSectionExpander(prompt3):
   response = openai.Completion.create(
   model="text-davinci-003",
   prompt="Expand the blog section in to the professional,witty and clever explanation:{} \n\f".format(prompt3),
   temperature=0.7,
   max_tokens=256,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
   )
   return response ['choices'][0]['text']

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Generate blog topics on:java",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# print(response)

