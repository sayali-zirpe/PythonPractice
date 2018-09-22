#from  flask import Flask ,jsonify,Response




user_profile=[

        {
            'timeline':[
                {
                    'home_timeline':[
                        {
                            'since_id':'since_id'
                            'max_id':'max_id'
                            'count':'count'
                            'page':'page'
                        }
                    ]
                    'statuses_lookup':[
                        {
                            'id':'id'
                            'include_entities':'include_entities'
                            'trim_user':'trim_user'
                            'map':'map'
                        }
                    ]

                    'user_timeline':[
                        {
                            'id':'id'
                            'user_id': 'user_id'
                            'screen_name':'screen_name'
                            'since_id':'since_id'
                            'max_id':'max_id'
                            'count' : 'count'
                            'page' : 'page'

                        }
                    ]

                    'retweets_of_me':[
                        {
                            'since_id':'since_id'
                            'max_id': 'max_id'
                            'count':'count'
                            'page':'page'
                        }
                    ]

                    

                }
            ]#timeline end


            'user_methods':[
                {
                    'get_user':[
                        {
                            'id':'id'
                            'user_id':'user_id'
                            'screen_name':'screen_name'
                        }

                        #user=api.get_user(screen_name=screen_name)
                        # user_id=user.id
                        #print(user_id).....user or json object format  or object list and then parse
                    ]

                    'me':[
                        {

                        }
                    ]

                    'followers':[
                        {
                            'id':'id'
                            'user_id':'user_Id'
                            'screen_name':'screen_name'
                            'cursor':'cursor'
                        }
                    ]

                }
            ]

            'friendship':[
                {
                    'show_friendship':[
                        {
                            'source_id':'source_id'
                            'source_screen_name':'source_screen_name'
                            'target_id':'target_id'
                            'target_screen_name':'target_screen_name'
                        }
                    ]
                    'friends_ids':[
                        {
                            'id':'id'
                            'screen_name':'screen_name'
                            'user_id':'user_id'
                            'cursor':'cursor'
                        }
                    ]

                    'followers_ids':[
                        {
                            'id': 'id'
                            'screen_name': 'screen_name'
                            'user_id':'user_id'
                            'cursor':'cursor'
                        }
                    ]


                }
            ]


            'account':[
                {
                    'verify_credentials':[
                        {

                        }

                    ]
                }
            ]



        }
    ]

]


    
