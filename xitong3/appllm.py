from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, load_tools, AgentType
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Set environment variables for API keys
os.environ["SERPAPI_API_KEY"] = '0fdf2243442ef59bb738c69fc6093c9901fdb3fb10b073653e254df558f9bc2a'

# Initialize the ChatOpenAI model
llm = ChatOpenAI(
    api_key="sk-a9f778112e4c486e8acf2502c5280068",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", 
    model="qwen2-1.5b-instruct"
)

# Load tools and initialize the agent
tools = load_tools(["serpapi"])
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    # 构建prompt，只回答医疗相关的问题
    prompt = f"I am a medical assistant designed to answer questions related to health and medicine. Please only ask me questions related to these topics. Your question: {user_input}"

    try:
        response = agent.invoke(prompt)
        print(response)
        if isinstance(response, dict):
            response_text = response.get('output', 'No response text')
        else:
            response_text = str(response)
        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)