import re;
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word (email, word):
  '''censor a single word'''
  if (word in email ): 
    email = email.replace(word, "*c*ns*r*d*")
  return email
# print(censor_word( email_one, "learning algorithms" ));
# first solution is not very efficient as it does not take into account the length of the phrase

def censor_phrase(email, phrase):
  '''Censor a single phrase and returns email'''
  censored = ''
  for i in range(len(phrase)):
    if phrase[i] == ' ':
      censored += ' '
    else:
      censored += '#'
  return email.replace(phrase, censored)
print(censor_phrase(email_one, "learning algorithms"));
#takes into account spaces

def censor_list(email, given_list):
  update_email = ''
  i = 0
  for term in given_list:
    censored = []
    while len(censored) < len(term):
      censored.append('*')
    censored_join = ''.join(censored)
    if i == 0:
      regex =  "\\b"+ term + "\\b"
      update_email = re.sub(regex, censored_join, email, flags = re.IGNORECASE)
      i += 1
    else:
      regex =  "\\b"+ term + "\\b"
      update_email = re.sub(regex, censored_join, update_email, re.IGNORECASE)
  return update_email
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]
print(censor_list(email_two, proprietary_terms))
#Takes into account case sensitivity but not spaces. Probably need to fix my regex/ 

def censor_lists(email, lst1, lst2):
  '''Censors all prioprietary terms and negative words and returns email'''
  update_email = ''
  i = 0
  k = 0
  for item in lst1:
    censored = []
    while len(censored) < len(item):
      censored.append('*')
    censored_join = ''.join(censored)
    string_item = str(item)
    regex =  "\\b"+ item + "\\b"
    tmp_lst = re.search(regex, email)
    if tmp_lst != None:
      i += 1
    if i >= 2:
      break
  for word in lst1:
    if i >=2 and k == 0 :
      regex = "\\b"+ word + "\\b"
      update_email = re.sub(regex, censored_join, email, flags = re.IGNORECASE)
      k += 1
    elif i >= 2 and k != 0:
      regex = "\\b"+ word + "\\b"
      update_email = re.sub(regex, censored_join, update_email, flags = re.IGNORECASE)
  update_email = censor_list(update_email, lst2)
  return update_email
negatives = [ "concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable", "The"] 
print(censor_lists(email_three, negatives,proprietary_terms))
#does the thing, but does not take into account spaces and the two negatives words that are allowed are not at the beginning as I inteneded (not sure that this matters though)

def censor_all(email, lst1, lst2):
  censor_email = censor_lists(email,lst1,lst2)
  split_email = censor_email.split(' ')
  new_split_email = []
  i = 0
  k = 0
  try:
    for word in split_email:
      if k < i:
        k += 1
        continue
      else:
        tmp_value1 = word.find('*')
        tmp_value2 = word.find('\n')
        if tmp_value1 == -1:
          if split_email[i + 1].find('*') != -1 :
            censored = []
            while len(censored) < len(word):
              censored.append('*')
            censored_join = ''.join(censored)
            new_split_email.append(censored_join)
            i += 1
            k += 1
          else:
            new_split_email.append(word)
            i += 1
            k += 1
        else:
          if tmp_value2 == -1:
            if split_email[i +1].find('*') == -1 :
              censored = []
              while len(censored) < len(split_email[i + 1]):
                censored.append('*')
              censored_join = ''.join(censored)
              new_split_email.append(word)
              new_split_email.append(censored_join)
              i += 2
              k += 1
            else:
              new_split_email.append(word)
              i += 1
              k += 1
          else:
            new_split_email.append(word)
            i += 1
            k += 1

  except IndexError:
    new_join_email = ' '.join(new_split_email)
    return new_join_email
print(censor_all(email_four,negatives,proprietary_terms))
  







