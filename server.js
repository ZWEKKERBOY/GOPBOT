//Requirements
const Discord = require('discord.js');
//Colors extends the string prototype
require("colors");
var config = require("./config.json");

const Manager = new Discord.ShardingManager('./bot.js');
console.log("Booting up Gopbot!".red)
//Display the invite link
console.log(`Bot invite link: https://discordapp.com/oauth2/authorize?client_id=${config.clientid}&permissions=8&scope=bot`.green);
//Spawn and maintain the amount of shards specified in the config
console.log(`Starting up ${config.shards} shard(s)!`.blue)
Manager.spawn(config.shards, 1);