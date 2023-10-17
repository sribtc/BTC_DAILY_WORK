# import vertexai
# from vertexai.language_models import ChatModel, InputOutputTextPair

# vertexai.init(project="sturdy-apricot-393915", location="us-central1")
# chat_model = ChatModel.from_pretrained("chat-bison@001")
# parameters = {
#     "candidate_count": 1,
#     "max_output_tokens": 256,
#     "temperature": 0.2,
#     "top_p": 0.8,
#     "top_k": 40
# }
# chat = chat_model.start_chat(
#     context="""You are an clinical decision support system, when the user comes with certain medical condition , you as the user for other symptom and classify the disease

# you consider all the diseases that are having these symptoms ,and then you only  ask the user question about these symptoms, and finally consider all his responses and classify the disease


# """,
# )
# response = chat.send_message("""Hello""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""i am having an head che""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""sure""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""in sides""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""sure""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""for past 1 week""", **parameters)
# print(f"Response from Model: {response.text}")
# response = chat.send_message("""yes""", **parameters)
# print(f"Response from Model: {response.text}")
