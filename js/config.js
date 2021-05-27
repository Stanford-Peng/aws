window._config ={
    cognito:{
        userPoolId: 'us-east-1_wR9mama0w',
        region: 'us-east-1',
        clientId: '4rrtmgavid4rq03c4s80uist78'
    },
    api:{
        uploadUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/upload',         //HTTP POST     JSON Format: {name:"xxxx.jpg", file:""}
        findByTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/findbytags', //HTTP POST     JSON Format: {tags: "["person", "elephant"]"}
        deleteUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/deleteimages',       //HTTP DELETE   JSON FORMAT: {name: ["xxxxx.jpg", "asdf.jpg"]}
        findTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/findtags',     //HTTP GET
        modifyTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/modify-tags',//HTTP POST     JSON FORMAT: {name: "xxx.jpg", tags: ["tag1", "tag2"]}
    }
};