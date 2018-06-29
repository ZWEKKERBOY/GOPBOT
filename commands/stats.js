const ip = require("ip");
const ms = require("ms");
module.exports = {
    'run': async function (msg, args, app) {
        try {
            msg.channel.send({
                embed: {
                    title: "Stats",
                    color: app.config.msgColor,
                    fields: [
                        {
                            "name": "Latency",
                            "value": `${app.client.ping}ms`
                        },
                        {
                            "name": "Server IP",
                            "value": ip.address()
                        },
                        {
                            "name": "Uptime",
                            "value": ms(app.client.uptime, { long: true })
                        },
                        {
                            "name":"Shards",
                            "value":app.config.shards
                        }
                    ]
                }
            });
        } catch (error) { console.log(error) }
    },
    'description': "Shows server stats",
    'arguments': [],
    'tags': []
};