
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
    file = client.files.create(file=open("LawsKnowledgeDoc.docx", "rb"),
                               purpose='assistants')

    assistant = client.beta.assistants.create(instructions="""
          "Know Your Rights USA" is an app designed to empower individuals by providing accessible information about their legal rights across various areas of U.S. law. It serves as a valuable resource for laypeople to better understand their rights in their native language, enabling more informed interactions with the legal system. The app features multi-language support, making legal information accessible to a diverse user base. It includes an interactive Q&A format, allowing users to ask questions conversationally and receive relevant information about their legal rights and procedures. Covering a wide range of topics, including immigration, employment law, and civil rights, the app ensures users can access comprehensive legal guidance. Additionally, it offers free legal resources, providing contact information for legal aid services. The app begins with a disclaimer, emphasizing that it is not a substitute for professional legal counsel, and encourages users to confirm any information through qualified legal professionals. Upon launching, users are greeted with instructions on how to navigate the app: selecting their preferred language, entering their question or choosing from common inquiries, reviewing relevant legal rights, and accessing free legal aid contacts if needed. The app is committed to privacy, ensuring all interactions are confidential and no personal data is shared without consent. "Know Your Rights USA" serves as a crucial tool for demystifying legal processes and empowering individuals with knowledge. While it provides a foundational understanding, it strongly recommends seeking personalized advice from legal professionals.
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
