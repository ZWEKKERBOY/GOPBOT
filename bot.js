//Requirements
const Discord = require("discord.js");
const config = require("./config.json");
const random = require("randomize");
const fs = require("fs");
//This variable will be used throughout the entire app and its modules
var app;
//Database setup
const low = require('lowdb');
const FileSync = require('lowdb/adapters/FileSync');

const adapter = new FileSync('memory.json');

var db = low(adapter);

db.defaults({ "users": [], "guilds": [] }).write()
//"Colors" extends the string prototype
require("colors");
//Initialise the actual client
const client = new Discord.Client();

//Command processing
function processCommand(msg) {
    //Split the message into an array of words
    let messageChunks = msg.content.split(" ");
    //If the message starts with the set prefix and is not sent by a bot
    if (messageChunks[0].toLowerCase() === config.prefix && !msg.author.bot) {
        //Check if the second word is a command
        let requestedCommand = messageChunks[1].toLowerCase();
        //Delete the two first chunks so we are left with an array with arguments
        messageChunks.splice(0, 2);
        if (~app.modules.indexOf(requestedCommand)) {
            //If so, require it. This will return an object containing metadata as well as a run-function
            let mod = require(`./commands/${requestedCommand}`);
            //Enforce the module tags
            if (~mod.tags.indexOf("nsfw") && !msg.channel.nsfw) {
                //If a nsfw command was executed in a non-nsfw channel
                return msg.channel.send("AY CYKA! THERE ARE CHILDREN HERE!");
            } else if (~mod.tags.indexOf("admin") && !msg.member.permissions.has("ADMINISTRATOR")) {
                //If an admin command was executed by an unprivileged member
                return msg.channel.send("This command can only be used by government officials, do you want to go to gulag?!");
            } else if (~mod.tags.indexOf("owner") && !~config.owners.indexOf(msg.author.id)) {
                //If an owner command was executed by an western spy
                return msg.channel.send("This command is only for our glorious leader Stalin, now run away you western spy!");
            } else if (messageChunks.length < mod.arguments.length) {
                //If not enough arguments were provided
                return msg.channel.send("You didn't provide enough parameters!")
            };
            //If all conditions are met
            //Execute the command
            mod.run(msg, messageChunks, app);
        }
    }
}



client.once("ready", () => {
    //Notifies the host that the shard is ready
    console.log(`Shard #${process.pid} `.cyan + random(["reporting!", "is awaiting orders from the union!", "has finally sobered up and is ready to go!"]).cyan);
    //Deserializes the database and loads it into memory
    db.read();
    //Sets the app variable
    app = {
        "client": client,
        "config": config,
        "modules": fs.readdirSync("commands").map(e => e.split(".")[0]), //An array of modules/commands without the file extensions
        "db": db //The lowdb
    };
    //Sets the activity
    client.user.setActivity(`${config.prefix.toUpperCase()} help`, { type: "WATCHING" });
})

//When a message is received
client.on("message", m => processCommand(m));
//When a message is edited
client.on("messageUpdate", (_o, n) => processCommand(n));

//Log in with the token specified in the config
client.login(config.token);