window._config ={
    cognito:{
        userPoolId: 'us-east-1_wR9mama0w',
        identityPoolId: 'us-east-1:caa1ec19-b4ce-4188-a6d3-dfd244ec662f',
        region: 'us-east-1',
        clientId: '4rrtmgavid4rq03c4s80uist78',
        googleClientId: '4bkavr8t1jvp2krihuvals3726',
        hostedUIUrl: 'https://image-detection-login.auth.us-east-1.amazoncognito.com/login?client_id=4rrtmgavid4rq03c4s80uist78&response_type=token&scope=phone+email+openid+aws.cognito.signin.user.admin+profile&redirect_uri=http://localhost:5500/html/main.html'
    },
    api:{
        uploadUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/upload',                 //HTTP POST     JSON Format: {name:"xxxx.jpg", file:""}
        findByTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/findbytags',         //HTTP POST     JSON Format: {tags: "["person", "elephant"]"}
        deleteUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/deleteimages',               //HTTP DELETE   JSON FORMAT: {name: ["xxxxx.jpg", "asdf.jpg"]}
        findTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/findtags',             //HTTP GET
        modifyTagsUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/modify-tags',        //HTTP POST     JSON FORMAT: {name: "xxx.jpg", tags: ["tag1", "tag2"]}
        findTagsByImageUrl: 'https://4t07pj5pkk.execute-api.us-east-1.amazonaws.com/dev/api/findtagsbyimage'//HTTP POST     JSON Format: {file:""}
    },
    google:{
        clientId: '939395917142-f9bmb97fv5jr60be20nahrrh8taer9f7.apps.googleusercontent.com',
    }
};