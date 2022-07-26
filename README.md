# Microservice-Implementation

Communication contract:

Requesting Data... First, you'll set up a python socket. I created a sample one in the fruit_client file. You need to send the you need to send a list of foods as a JSON. It does not matter how long the list is, but if you have fruits that you want to identify that aren't in the fruit_server file, you'll have to add them. 

Receiving Data...The server will take the list and check it against a list of fruits. Then it will return data as JSON in a list of booleans. The list indicated True for fruits and False for non-fruits. The server will return an error if something goes wrong. 

![server-client](https://user-images.githubusercontent.com/83997457/180904410-1fae6f22-db16-4cd2-9f50-37c75bb6cf7b.png)
