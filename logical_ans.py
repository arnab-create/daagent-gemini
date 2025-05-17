def run():
   
    from google import genai
    import json

    with open("api.txt") as f:
        api=f.read()
    client = genai.Client(api_key=api)


    myfile = client.files.upload(file="bank_metadata.csv")

    
    with open("question.txt") as f:
        question=f.read()

    response = client.models.generate_content(


        model="gemini-2.0-flash", contents=['"You are data analyst. Please provide a suitable narrative to the question to the requestor:' + question + '"', myfile]
    )
 
    print("Following are Tables and Attributes identified to answer your query")

    print(response.text)

    ss=response.text

    ss = ss.replace("```json", "")
    ss = ss.replace("```", "")

    with open('ipsql.json', 'w') as json_file:
        json_file.write(ss)

