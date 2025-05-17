def run():
    import json
    from google import genai


    # Opening JSON file
    f = open('ipsql.json')

    # returns JSON object as a dictionary
    data = json.load(f)

    tables=''
    # Iterating through the json list
    for i in data['tables']:
        tables=',' + i + tables


    columns=''
    # Iterating through the json list
    for i in data['columns']:
        columns=i +', ' + columns

    # Closing file
    f.close()

    with open("api.txt") as f:
        api=f.read()
    client = genai.Client(api_key=api)

    myfile = client.files.upload(file="bank_metadata.csv")

    with open("question.txt") as f:
        question=f.read()

    print("Generating SQL via gemini-2.0-flash")

    
    response = client.models.generate_content(


        model="gemini-2.0-flash", contents=['"You are a Data Analyst. You are expected to only output executable  SQL query. Write a MySQL equivalent SQL query based on the identified tables' + tables + 'and columns ' + columns + ' to answer the question : ' + question +'"' ]
    )

    
    print(response.text)



    ss=response.text

    ss = ss.replace("```sql", "")
    ss = ss.replace("```", "")

    with open('opsql.txt', 'w') as json_file:
        json_file.write(ss)

