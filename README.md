# Bot-Template Repository
**by Greeny**

This repository is for me and for everyone who wants to start coding discord bots with Py-Cord (Python).
I'll provide a short instruction to help you starting.
If you need any help please contact me on discord: @greenydev.

### CONSIDER
This is not an official template from Py-cord developers. It is essentially a template for myself so that I don't have to start from scratch with every bot. 
Optimizations & improvements will be made as soon as necessary.

### Requirements
- Installed Python Version 3.11 or below (NOT 3.12!)
- Visual Studio Code or another coding app
- Discord Account and a own server with admin permissions

## STEP ONE: Create a discord bot
Open the [Discord Developers Website](https://discord.com/developers/applications)

Click on "New Application" on the top right corner of the website:

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/f88de3e0-eaf5-4b10-9547-0a7a1b304d0f)

Enter a powerful name and accept the ToS:
![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/ac5b471b-de1d-41b2-96a1-745a0a8c10e4)

Now you're on the dashboard of your own discord bot. Go to the tab "Bot".
You can give your bot a profile picture and a banner. But that's up to you.
We're only interested in the privileged gateway intents. Activate the three options from the picture below:

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/bb7ab41d-05d6-43d1-84b4-fd60c9d5bba0)

**Don't forget to save your changes!**

Next, go to the tab 0Auth2 and scroll down to "URL Generator". Select >bot< and >application.commands<:

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/fdcf3166-0069-42c7-b0e0-0cf2cd0225e2)

Scroll down again and select the permissions you bot should have or need. For my testbo I'll just select "Administrator".

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/8a0b9878-a8e3-4928-a729-c76f7430befb)

After you've selected your permissions right, click "copy" on the left bottom corner like int the picture above. This is your link to invite your bot to your server!

## STEP TWO: Invite your bot

Open a new tab in your browser and insert your copied link. 

```bash
https://discord.com/oauth2/authorize?client_id=1237722887935234078&permissions=8&scope=bot+applications.commands
```
This is the link of my test bot. Your link should look similar to this one. 
When you open the site you should come to this window:

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/df12a785-a973-4621-9a4b-d0bd331f97bc)

Select your server where you wanna invite your bot. 

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/6c9a3088-e23f-4ea4-9d2c-9bcccbf8f2de)

Click "continue" and authorize the access to your server:

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/5809ea42-4975-4ba0-a2ab-09b7b5a874bc)

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/40823982-9437-447d-9ce0-09f5a59d81ba)

When you open your own discord server, you should see, that the bot joined it. 

![image](https://github.com/greenyydev/PyCord-Bot-Template_Greeny/assets/65386324/61d27c29-732e-4d72-82d5-b688608e2ade)

## STEP THREE: Download the Repository and bring your bot online

Open Visual Studio Code or another developing application. If you don't know how to clone a repository just download a zip or search for a tutorial on how to download and clone github repositorys.

![image](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/f91211c3-b52e-4445-a749-638c7d9f57eb)

So, the repository is opened and you see the code. Next, go back to your Developer Portal and the Bot tab. 
Klick "Reset Bot Token":

![image](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/b84aeabe-4063-400f-931b-fb30d1026036)

Copy your token by clicking the button. 

![bottoken](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/daf6d607-d46f-45df-982f-81005cd4d269)

Now go to your developing application and open the .env file:

![image](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/6b68aa89-12c9-4035-9da8-618de4394a2b)

Paste your copied token behind the "TOKEN = " text. 
Once done, close the .env file again and move to main.py. 
All you have to do left is to execute this file. 

![image](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/1b173c40-b0ce-4a4c-ae63-5f871ea55c49)

![image](https://github.com/greenyydev/Discord-Bot-Template---PyCord/assets/65386324/6de916f6-8645-45d3-ad06-dd7870b669c5)

### Your Bot should be online!

If you need any help with issues or problems, please contact me on discord: @greenydev
