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

## STEP TWO: Invite your bot and bring it online

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

