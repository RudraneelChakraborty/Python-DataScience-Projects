**Book Management System with AI summary and Recommendation based on Book Genre**

Steps to run ->
1. Through Direct Run ->
   a. Create a virtual environment.
   b. Run pip install -r requirements.txt
   c. Run python main.py
   d. The application will run on localhost:8001
   e. Check the health of the application by going http://localhost:8001/health_check
2. Through Docker Image ->
   a. Change the HOST of config.ini to "host.docker.internal"
   b. If docker is installed in the system run -> docker build <IMAGE_NAME> .
   c. The Dockerfile and dockerignore are already present.
   d. Once the image build is done, Run docker run -d -p 8001:8001 --network host <IMAGE_NAME>
   e. Also configure the docker network if the database connection is not happening from Local, Check TCP/IP of Local put that in config.ini and try again.

**LLM Services:**
1.	Install OLlama to run the LLAMA3 locally, https://ollama.com/ 
2.	Once installed open Terminal / CMD and run: ollama run llama3 
3.	It will download LLAMA3:8b instruct pre-trained version which will be pre-quantized to 4-bit version. https://ollama.com/library/llama3 
4.	Once done check if the Ollama running or not by going: http://localhost:11434/
The generate summary endpoint can be used by giving book content O, We can just specify the Book Name the content is automatically pulled from the Wikipedia page to show the summary.

Also, the Prompt Template is content aware means if somebody gives any other things other than Books Like even the Book Author's name then also it will say the AI Bot is for Book summary not for any other discussion.
*NOTE* - If the Ollama takes more time to give a response there is nothing to do from CodeBase, The Hardware of the Computer/Laptop Itself is not good enough to run LLM locally. The Ollama can run CPU only but that will be too much latency, Try to run in good GPU e.g. NVIDIA T4 or RTX 2080 TI at least.

If the Book Name  is not given and the Book Content is below 30 characters then it will show not enough content to summarise.

**Book Management System:**
All the specified endpoints will be available on the Swagger page, I have used Oracle Database to create both tables and books and review the creation script given with the CodeBase (oracledb.sql).
For Configs of the database, the config.ini and connectors will have to be set up. In my codebase, those are setup for my Oracle DB instance. Please change the config.ini file with the required parameters to connect with your own Oracle Instance.
Once that is set up, then someone can go to the docs page of Fast API and check the responses from Swagger UI.

**ML Book Recommendation:**

The Endpoint will take the book name as requested and provide the recommendation on top of that. It checks the name by Levenstein Distance to fetch the most similar book available in the dataset and then it fetches the Nearest Match on top of that and gives 5 book recommendations where the genre and ratings are high.
 
