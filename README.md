# danu-agent
Experiments with creating an AI assistant

## Getting started
Do these steps from the top level directory:
```
python -m venv venv
venv\scripts\activate
cd src\danu
pip install -r requirements.txt
pip install -e .
```
### Activate the virtual environment
A virtual environment in Python is like a project workspace where libraries are installed. We created one above, and we need to set up our editor and command line to use this newly created virtual envionment.  Here are instructions for doing that in Visual Studio code:

1. Open your workspace (the project you're working on) in VS Code.

2. Press Ctrl+Shift+P (on Windows/Linux) or Cmd+Shift+P (on macOS) to open the Command Palette.

3. Start typing "Python: Select Interpreter" in the Command Palette and select it when it appears.

A list of discovered Python interpreters will be displayed at the bottom of your window. This list will include any virtual environments located inside the workspace.

If your new environment is in the list, click on it to select it. If not, click on "Enter interpreter path" then "Find..." and navigate to the Python executable in your virtual environment. The exact location will depend on where you created your virtual environment, but the path should end with something like /venv/bin/python on Unix/macOS or \venv\Scripts\python.exe on Windows.



# Danu Agent
> I would like to make a program that can read all of my OneNote documents (which are stored in a combination of OneDrive and Sharepoint) as well as my emails. What would be a good way to approach this? I'm wondering if this is the sort of thing the Graph API is designed for.

Tprompt (GPT4 plus all the Azure Documentation) says:
> Yes, the Graph API is designed for this purpose. You can use Microsoft Graph API to access your OneNote documents stored in OneDrive and SharePoint, as well as your emails[2]. To get started, you can follow a tutorial on accessing Microsoft Graph from a web app for a signed-in user[1]. This will help you grant delegated permissions to your web app and call Microsoft Graph from the web app for a signed-in user.
> For OneNote documents, you can access the DriveItem resource in Microsoft SharePoint and OneDrive[2]. For emails, you can access the Message resource in Microsoft Outlook[2]. Make sure to grant the necessary permissions to your application to access these resources.
Remember to follow best practices and handle authentication and authorization securely when building your program. Good luck!


Resources:

* [Microsoft Graph overview](https://learn.microsoft.com/en-us/graph/overview)
* [Use the Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api)
* [Accessing microsoft Graph with user permissions](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/active-directory/develop/multi-service-web-app-access-microsoft-graph-as-user.md)
* [Partner events in Graph API](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/event-grid/partner-events-graph-api.md)

# Research Roadmap
These are the basic milestones I'm covering. We will approach the biggest key risks first.  I want a conversational agent which spins up a graph of sub agents and conversation contributors searching vector databases and other resources, and taking actions, and so on.  To focus our efforts we will do research in segments with goals for each milestone:
1. **Graph API basics**. Ability to read my personal one note files under program control.
2. **Vector DB all one note things**
3. **Personal agent.** Chat with agent, and integrate memories from my one note docs

