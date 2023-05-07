/*
  food.js -- Router for the food finder
*/
const express = require('express');
const router = express.Router();
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);



isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }


router.get('/food',
    isLoggedIn,
    (req,res,next) => {
    res.render('food');
   })

router.post('/food',
async (req,res,next) => {
     console.log('getting food')
     res.locals.food = req.body.food
     res.locals.info = await get_info(req.body.food)
     res.render('foodInfo')
})

const get_info = async (food) => {
    const prompt = "What are healthier alternatives to the food: "+food;
    const completion = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: prompt,
        max_tokens: 1024
    });
    console.log(completion.data.choices[0].text);
    return (completion.data.choices[0].text)
  }


module.exports = router;
