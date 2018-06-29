const random = require("randomize");

module.exports = {
    'run': async function (msg, args, app) {
        try {
            let helpBody = "";
            //Iterate over all modules and add them to the embed body
            app.modules.forEach(modName => {
                //Require the module
                let mod = require(`./${modName}.js`);
                //Append a description of the command
                helpBody += `\`${app.config.prefix.toUpperCase()} ${modName.toUpperCase()}\` ${mod.arguments.length ? "[" + mod.arguments.toString() + "]" : ""} - ${mod.description}`
            });
            //Send the actual embed
            msg.author.send({
                "embed": {
                    color: random([0xff0000, 0xffffff, 0x0065ff]),
                    description: ":regional_indicator_g: :regional_indicator_o: :regional_indicator_p: :regional_indicator_b: :regional_indicator_o: :regional_indicator_t:",
                    fields: [
                        {
                            "name": "INFORMATION",
                            "value": "The GOPBOT is ready to squat down, drink and have some fun. It can do some cheeki breeki commands and welcomes you the slav way!"
                        },
                        {
                            "name": "COMMANDS",
                            "value": helpBody
                        },
                        {
                            "name": "NOTES",
                            "value": `
To get GOPBOT welcoming slavs the slavic way, you'll need a textchannel named ‘welcome’  where it has the rights to send messages!
`
                        }
                    ],
                    timestamp: new Date(),
                    footer: {
                        icon_url: app.client.user.avatarURL,
                        text: "Thank you for using GOPBOT. Stalin would be proud of you!"
                    }
                }
            })
        } catch (error) { console.log(error) }
    },
    'description': "Shows this menu, what did you expect cyka?",
    'arguments': [],
    'tags': []
};