#Configuration File

from  flask import Flask ,jsonify,Response

app=Flask(__name__)


#source_type:value

#source_type=[Twitter,Facebook,Google,Linkedin]
#value=[twitter_api_path,.....]
#value=api_url
#field_input:value
#field_input=[username ,userid,description,url,location,statuses count, statuses,followers count,followers_ids,
#followers,friends count,friends ids]

#value:call particular method or pass parameters to that api file or method


twitter_api="file path or import????"
facebook_api=""
google_api=""
google_api=""
linkedin_api=""


def source_apis():
    source = {
        twitter:
        facebook:
        google:
        linkedin:
    }

     return jsonify ({'msg':'successful'})


def twitter_source_field():
    fields = {
        username:method call
        userid:
        description:
        url:
        location:
        statuses count:
        statuses:
        followers count:
        followers_ids:
        followers:
        friends count:
        friends ids:
    }


     return jsonify ({'msg':'successful'})


def facebook_source_field ():
    fields = {



    }


    return jsonify ({'msg':'Facebook source fields sent'})


def google_source_field ():
    fields = {



    }


    return jsonify ({'msg':'Google source fields sent'})


def linkedin_source_field ():
    fields = {



    }


    return jsonify ({'msg':'Linkedin source fields sent'})


app.run(port=5000)




    
