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


        model="gemini-2.0-flash", contents=['"You are a Data Analyst. Based on the attached metadata file(bank_metadata.csv) please identify the tables and columns that will be required to answer the following question. Tables identified returns in table wrapper and columns identified returns in column wrapper. Return the result as json:' + question + '"', myfile]
    )
 
    print("Following are Tables and Attributes identified to answer your query")

    print(response.text)

    ss=response.text

    ss = ss.replace("```json", "")
    ss = ss.replace("```", "")

    with open('ipsql.json', 'w') as json_file:
        json_file.write(ss)
