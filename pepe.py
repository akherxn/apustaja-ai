def tweeter():    
    import codecs
    from pkg_resources import ContextualVersionConflict
    from main import api, os, time
    from replier import reply 
            
    def cant_be_helped():
        # for unexpected errors
        print("hibernating because it can't be helped") 
        time.sleep(1000000)
 
    def tweet_sender():
        t = codecs.open('tweets.txt', 'r+', 'utf-8') 
        readlines_ = t.readlines()
        t.close()
        for line in readlines_:
            print("checking:" + line)
            try:
                results = api.search_tweets(q=line, tweet_mode='extended')
                for result in results:
                    processed_result = result.full_text + '\n'
                    if result.user.screen_name == 'apustaja_ai' and line == processed_result:
                        try:
                            readline_index1 = readlines_.index(line) 
                            del readlines_[readline_index1]
                            n1 = codecs.open('tweets1.txt', 'w', 'utf-8')
                            n1.writelines(readlines_)
                            n1.close()
                            os.remove('tweets.txt')
                            os.rename('tweets1.txt', 'tweets.txt')
                            print("deleted the sneaky duplicate")   
                        except Exception as result_err1:
                            print(result_err1)
                            pass        
                    elif line == processed_result:
                        try:
                            readline_index3 = readlines_.index(line)
                            del readlines_[readline_index3]
                            n2 = codecs.open('tweets1.txt', 'w', 'utf-8')
                            n2.writelines(readlines_)
                            n2.close()
                            os.remove('tweets.txt')
                            os.rename('tweets1.txt', 'tweets.txt')
                            print("deleted duplicate line [similar tweet]") 
                        except Exception as result_err3:
                            print(result_err3)
                            pass                
                    else:                   
                        print("all set")     
            except Exception as wut:
                print(wut)
                pass        
            try:
                print("posting ...")
                tweeted_status = readlines_[0]
                shitpost = api.update_status(tweeted_status)         
                print(tweeted_status)
                del readlines_[0]
                n5 = codecs.open('tweets1.txt', 'w', 'utf-8')
                n5.writelines(readlines_)
                n5.close()
                os.remove('tweets.txt')
                os.rename('tweets1.txt', 'tweets.txt')
                
                print("deleted:  " + tweeted_status)
                try: 
                    if os.path.exists('tweet_id.txt'):
                        os.remove('tweet_id.txt')
                    iid = codecs.open('idd.txt', 'w', 'utf-8')
                    instr = str(shitpost.id)
                    iid.write(instr)
                    iid.close()
                    os.rename('idd.txt', 'tweet_id.txt')
                    print("updated tweet_id.txt")
                except Exception as write:
                    print(write)
                    cant_be_helped()
                
            except Exception as status_err:
                print(status_err)
                time.sleep(5)
                pass
                
            print("sleepin for 2 hrs")
            le_count = 0
            while le_count < 18:
                reply()
                le_count = le_count + 1
                time.sleep(400)
            tweeter()
            
            
    print("Fetched statuses for checking post.title duplicate")
    if os.path.exists('tweet_id.txt'):
        print("reading tweet_id.txt")
        re = codecs.open('tweet_id.txt', 'r+', 'utf-8')
        re.readlines()
        re.close()
        tweet_id_ = int(re[0])
    else:
        print("tweet_id.txt not available")
        tweet_id_ = None
    statuses = api.user_timeline(count=1, 
                                 include_rts=False, 
                                 exclude_replies=True, 
                                 screen_name='apustaja_ai', 
                                 tweet_mode='extended')
    print(str(len(statuses)) + " statuses fetched")
    if len(statuses) == 0:
        tweet_sender()
    m = codecs.open('tweets.txt', 'r+', 'utf-8')
    lines_in_textfile = m.readlines()
    # set_of_lines = set(lines_in_textfile) 
    for tweet in statuses:
        # j = [tweet.full_text+"\n"]
        full_tweet = tweet.full_text+"\n" 
    # j2 =set(j)
    # print(j2) 
    # print(full_tweet)         
    # if j2.issubset(set_of_lines) == True:
    m.close()
    
     
    # sets do not preserve the order of elements in it, I'll use the list instead to prevent deleting untweeted lines. 
    if (full_tweet in lines_in_textfile): 
        try:
            print("found duplicate")       
            full_tweet_index = lines_in_textfile.index(full_tweet)
            del lines_in_textfile[:full_tweet_index+1] 
            # n = codecs.open('tweets.txt', 'r+', 'utf-8')
            # read_lines = n.readlines()
            # line_index = read_lines.index(j[0])
            index_string = str(full_tweet_index)
            print("index: " + index_string)
            # del read_lines[:line_index+1]
            nn = codecs.open('tweets1.txt', 'w', 'utf-8')
            nn.writelines(lines_in_textfile)
            nn.close()
            os.remove('tweets.txt')
            os.rename('tweets1.txt', 'tweets.txt') 
            print("deleted:  " + full_tweet)
            time.sleep(5)
            tweeter()
           
        except Exception as dafuq:
            print(dafuq)
            tweeter()
    else:   
        print("no duplicates")
        tweet_sender()
        
              
            
   
                
       
        
        

       


      

    

       
