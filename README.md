<table>
  <tr>
    <td><h2>ChordAuth</h2></td>
    <td><img src="https://raw.githubusercontent.com/SeafoodStudios/ChordAuth/main/resources/logo.png" alt="ChordAuth Logo" width="80"/></td>
  </tr>
</table>

ChordAuth is a _decentralized_ **authentication** and **storage** protocol where the client _really_ owns their data.

All the ChordAuth protocol requires is a **public key**, which is like your _username_, and your **private key**, which is your _password_. The private key is never required by any server, and is instead used for creating a signature, which is basically revealing that you are in fact, you, without revealing anything secret. Nobody needs to trust the other end, because using this protocol, this is possible. 

It works like this:
1. The server authenticates the client by checking their signature against their public key.
2. The server can then create an account on the client's computer.
3. All the server stores is the API key, which is its password to the client's storage group.
4. Whenever the server needs to store something, the client starts a server on their end, and connects to the server, allowing data to be exchanged.
5. The client can always revoke the server's access in case the server is using too much data or misbehaving.

## Installation

You can install ChordAuth on your laptop by following these instructions):

1. First, **install ChordAuth by running ```pip3 install chordauth```** in your [command line application](https://www.w3schools.com/whatis/whatis_cli.asp).
2. Then, **create your account by running ```chordauth server```**. It should ask you a series of questions, like picking a password and choosing a [file path](https://www.codecademy.com/resources/docs/general/file-paths). You can find your desired file paths by looking for a file path that does not exist (that should be relatively easy).
3. If you did things correctly in the previous step, it should start a pinggy server. Pinggy servers are merely a relay for the protocol and are replaceable. You should now **open a new command line window and run ```chordauth dashboard``` and fill in the inputs.** The server link should be the pinggy server link (you can find the link in the "chordauth server" command line prompt).
4. **You should recieve a warning when you open [https://127.0.0.1:5002/](https://127.0.0.1:5002/)**. This is because this is a self signed local development server, and the browser thinks it is not safe. You can bypass this warning. It should then give an error. This is because a server needs to create a storage group on your laptop first.
5. You can now **close both windows**.
6. In the future, when a server creates a storage group on your laptop, **you can monitor/remove it by running ```chordauth server```, filling in the inputs, running ```chordauth dashboard``` in a new window and opening [https://127.0.0.1:5002/](https://127.0.0.1:5002/)**, the dashboard.
