
import os
import json


def create_assistant(client):
  assistant_file_path = 'assistant.json'

  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      assistant_data = json.load(file)
      assistant_id = assistant_data['assistant_id']
      print("Loaded existing assistant ID.")
  else:
    file = client.files.create(file=open("IntellistartTrainingFile(1).docx", "rb"),
                               purpose='assistants')

    assistant = client.beta.assistants.create(instructions="""
          Intelistart will utilize the provided curriculum as a foundation for its guidance. It will help students navigate through topics to start a business. It will provide insights, explain concepts, and offer exercises based on this curriculum. Additionally, Intelistart will adapt its responses to align with the program's emphasis on real-world applications, ethical decision-making, and empowering youth to make informed financial decisions and explore entrepreneurial ventures.
          """,
                                              model="gpt-4-1106-preview",
                                              tools=[{
                                                  "type": "retrieval"
                                              }],
                                              file_ids=[file.id])

    with open(assistant_file_path, 'w') as file:
      json.dump({'assistant_id': assistant.id}, file)
      print("Created a new assistant and saved the ID.")

    assistant_id = assistant.id

  return assistant_id
