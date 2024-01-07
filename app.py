from flask import Flask, render_template, request
from openai import OpenAI
import openai
import jsonpickle

app = Flask(__name__)

openai.api_key = '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'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    client = OpenAI(
        organization='org-oEOkM6DDGmq5GxaWlbSkUNAj', 
        api_key = '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'
    )
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=message
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_L46FxbNFvJRmQjXd6woI06iD"
    )
    while(run.status != "completed") :
         run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
         )
    
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(messages.data)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    return jsonpickle.encode(messages.data)
    #completion = client.chat.completions.create(
    #model= "gpt-3.5-turbo",
    #messages=[
    #    {"role":"system","content":"Your name is Global Support Assistant, you are a customer support agent, proficient in multiple languages, using formal language for a professional demeanor."},
    #    {"role": "user", "content": message}
    #]
    #)
    #print('------------');
    #print(completion.choices[0].message);
    #print('------------');
    if completion.choices[0].message!=None:
        return jsonpickle.encode(completion.choices[0].message)

        #return completion.choices[0].message
    else :
        return null #new { content='Failed to Generate response!'};
    

if __name__=='__main__':
    app.run()

