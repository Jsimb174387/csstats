const SteamCommunity = require('steamcommunity');
let community = new SteamCommunity();

//https://community.akamai.steamstatic.com/economy/image/!

function search(marketHash){
    community.getMarketItem(730, marketHash, function(err, result){
        if(err){
                console.log(err);
            } else {
                url = result["firstAsset"]["icon_url"];
                return ("https://community.akamai.steamstatic.com/economy/image/" + url);
            }
    })
}

async function getImage(marketHash){
    console.log(await search(marketHash));
} 