#!/usr/bin/env python
#-*-coding:utf8-*-

from lxml import etree
from multiprocessing.dummy import Pool
import requests
import time

pool = Pool(4)
results = pool.map()
pool.close()
pool.join()
#在chrome中审查元素直接右键copy xpath可以直接得到xpath

html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Dating Web Site Assessment</title>
  </head>
  <body>
    <h1>Please Enter Your Details For Our Dating Websites!</h1>
    <form class="" action="https://ihome.ust.hk/~rossiter/cgi-bin/show_everything.php" method="post" enctype="multipart/form-data">

      <fieldset>
          <legend>Your Face</legend>
          <label for="avatar">Your Image:</label>
          <input type="file" id="avatar" name="name" value="">
          <br>
          Image Preview:
          <img src="" alt="" id="preview" />
      </fieldset>
      <fieldset>
          <legend>Your General Details</legend>

          <label for="fullname">Name:</label>
          <input type="text" id="fullname" name="name" placeholder="Your full name">
          <br>
          <label for="">Gender:</label>
          <input type="radio" id = "male" name="gender" value="">
          <label for="male">Male</label>
          <input type="radio" id = "female" name="gender" value="">
          <label for="female">Female</label>
          <br>
          <label for="age">Age:</label>
          <input type="number" id="age" name="name" value="18">
          <br>
          <label for="birthday">Date of birth:</label>
          <input type="date" id="birthday" name="name" value="">
          <br>
          <label for="">Favorite color:</label>
          <input type="color" name="name" value="">
          <br>
          <label for="">Which country:</label>
          <select class="" name="">
            <option value="option">America</option>
            <option value="option">UK</option>
            <option value="option">China</option>
            <option value="option">Germany</option>
            <option value="option">France</option>
            <option value="option">no selection</option>
          </select>
      </fieldset>
      <fieldset>
          <legend>Your Indicators</legend>
          <label for="">Height:</label>
          Short<input type="range" name="name" value="" min="0" max="100">Tall
          <br>
          <label for="">Salary</label>
          Poor<input type="range" name="name" value="" min="0" max="100">Rich
      </fieldset>
      <fieldset>
          <legend>Your Contact Information</legend>
          <label for="email">Email:</label>
          <input type="email" id="email" name="name" value="">
          <br>
          <label for="mobile">Mobile:</label>
          <input type="tel" id="mobile" name="name" value="">
          <br>
          <label for="address">Address</label>
          <textarea name="name" id="address" rows="2" cols="20"></textarea>
          <br>
          <label for="">Method to contact you:</label>
          <input type="checkbox" name="name" value="">Email
          <input type="checkbox" name="name" value="">Whatsapp
          <input type="checkbox" name="name" value="">In-app chat
      </fieldset>
      <input type="submit" name="name" value="Submit">

    </form>
  </body>
</html>
'''

response = requests.get('http://www.hunantv.com')

selector = etree.HTML(html)

content = selector.xpath('//option/text()')


for each in content:
    print each

# print response.text