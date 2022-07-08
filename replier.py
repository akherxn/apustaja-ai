def reply():
  import codecs
  from ntpath import join
  from main import api, tweepy, last_seen_mention_id, time
  import os
  import openai
  openai.api_key = os.environ["openai"]

  print("===================")

  for tweet in tweepy.Cursor(
          api.mentions_timeline, 
          count=5, 
          since_id=last_seen_mention_id, 
          tweet_mode="extended").items():
      last_seen_mention_id = tweet.id
    

      if tweet.user.screen_name != 'apustaja_ai' and tweet.favorited == False:
          print('\nreplying to ' + tweet.user.screen_name + '...')
          print('last seen mention ID: ' + str(last_seen_mention_id) + '\n')
          ftext = tweet.full_text.lower()
          ftext2 = ftext.split(" ")
          ftext3 = [ft for ft in ftext2]
          bd = '@apustaja_ai'
          if bd in ftext3:
            ftext3.remove(bd)  
          ftext3 = " ".join(ftext3)
          print(ftext3)
          instruct = 'write a short reply to the text below.'+'\n'
          full_prompt = instruct + ftext3 
          response = openai.Completion.create(
            model="text-davinci-002",
            prompt=full_prompt,
            temperature=0.7,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            echo=False
          )
          responses = response['choices'][0]['text']
          print(responses)
          length_of_response = len(responses)
          print(length_of_response)

          if length_of_response > 280:
            print("thread")
            try:
              try:
                splitted_response = responses.split("@")
                at_remover = [word_ for word_ in splitted_response]
                amogus = "".join(at_remover)
                print("removed '@'")
              except Exception as split_err:
                print(split_err)
                amogus = responses
              parts=amogus.split(" ")
              re1=[word for word in parts]
              ttt = "—"
              try:
                if ttt in re1:
                  kllr = re1.index(ttt)
                  del re1[:kllr]
                  print("removed the quote dash and everything after it")
                else:
                  pass
              except Exception as kllrerror:
                print(kllrerror)
                pass
                
              re2=re1[:31]
              status1=" ".join(re2)
              try:
                re3=re1[31:61]
                status2=" ".join(re3)
              except Exception as fail1:
                print(fail1)
                re3=re1[31:]
                status2=" ".join(re3)
              try:
                re4=re1[61:91]
                status3=" ".join(re4)
              except Exception as fail2:
                print(fail2)
                re4=re1[61:]
                status3=" ".join(re4)
              try:
                re5=re1[91:121]
                status4=" ".join(re5)
              except Exception as fail3:
                print(fail3)
                re5=re1[91:]
                status4=" ".join(re5)
              try:
                re6=re1[151:]
                status5=" ".join(re6)
              except Exception as fail4:
                print(fail4)
                pass
                
               
              if 'downvote' in tweet.full_text.lower():
                api.update_status_with_media(
                    status="no", 
                    filename='195.jpg', 
                    in_reply_to_status_id = tweet.id, 
                    auto_populate_reply_metadata = True)
                api.create_favorite(tweet.id)
                print("downvoted")
              else:
                try:
                  first_one=api.update_status(
                      status = status1, 
                      in_reply_to_status_id = tweet.id, 
                      auto_populate_reply_metadata = True)
                  api.create_favorite(tweet.id)
                  time.sleep(4)
                except Exception as slob69:
                  print(slob69)
                  pass
                
                
                # I'm trying to format a thread here for extra characters.
                # not sure if it's the right way. 
                try:
                  second_one=api.update_status(
                      status = status2, 
                      in_reply_to_status_id = first_one.id, 
                      auto_populate_reply_metadata = True)
                  time.sleep(4)
                except Exception as slob2:
                  print(slob2)
                  time.sleep(4)
                  pass
              
                try:
                  third_one=api.update_status(
                      status = status3, 
                      in_reply_to_status_id = second_one.id, 
                      auto_populate_reply_metadata = True)
                  time.sleep(4) 
                except Exception as slob:
                  print(slob)
                  time.sleep(4)
                  pass
              
                try:
                  fourth_one=api.update_status(
                      status = status4, 
                      in_reply_to_status_id = third_one.id, 
                      auto_populate_reply_metadata = True)
                  time.sleep(4) 
                except Exception as slob3:
                  print(slob3)
                  time.sleep(4)
                  pass
              
                try:
                  api.update_status(
                      status = status5, 
                      in_reply_to_status_id = fourth_one.id, 
                      auto_populate_reply_metadata = True)
                  time.sleep(4) 
                except Exception as slob4:
                  print(slob4)
                  time.sleep(4)
                  pass  

            except Exception as rq:
              print(rq)
              print("sleeping")
              time.sleep(10)
              pass

          else:
             
            if 'downvote' in tweet.full_text.lower():
              api.update_status_with_media(
                  status="no", 
                  filename='195.jpg', 
                  in_reply_to_status_id = tweet.id, 
                  auto_populate_reply_metadata = True)
              api.create_favorite(tweet.id)
              print("downvoted")
            else:
              try:
                print("not thread")
                try:
                  pots = responses.split("@")
                  potslist =[pot for pot in pots]
                  ots = "".join(potslist)
                  print("removed '@'")
                except Exception as potserr:
                  print(potserr)
                ots = responses
              
                pa1ts=ots.split(" ")
                re0=[word for word in pa1ts]
                rer=" ".join(re0)
                api.update_status(
                    status = rer, 
                    in_reply_to_status_id = tweet.id, 
                    auto_populate_reply_metadata = True)
                api.create_favorite(tweet.id)
              
              except Exception as r:
                print(r)
                print("sleeping")
                time.sleep(10)
                pass

 
  