from func import bot_function

no_avatar = 'https://support.discord.com/hc/user_images/l12c7vKVRCd-XLIdDkLUDg.png'

menu_list = {
    'bubbletea':' is enjoying a cup of bubbletea! :bubble_tea:',
    'coffee':' is enjoying a hot cup of coffee!',
    'cappucino':' is having a cup o\' cappucino!',
    'panipuri':' is having a hot panipuri! :yum:',
    'samosa':' is eating a spicy samosa! :yum:',
    'hotchocolate':' is enjoying some hot hotchocolate! :chocolate_bar:',
    'tea':' is having a chill cup of tea! :tea:',
    'smoothie':' is enjoying his/her smoothie!',
    'sushi':' is eating an exotic sushi!',
    'muffin':' is having a muffin!',
    'cake':' loves his/her cake! :cake:',
    'pancake':' is having a hot sweet pancake! :pancakes:',
    'icecream':' is enjoying a smooth and tasty icecream! :ice_cream:',
    'pizza':' is enojoying a cheesy pizza! :pizza:'
}


insult_quotes = [
    '<user> use your brain while talking, oh wait you don\'t have one.',
    '',
]


bot_function('help', None, 'For help on other functions','Use this function to get help related to other functions', '/help <command_name>')
bot_function('clear', ['manage_messages'], 'To clear recent messages','Use this function to clear recent messages!', '/clear <amount(optional)>')
bot_function('info', None, 'To get info about anyone!','Use this function to get information about any user on the server', '/info <member_mention>')
bot_function('eat', None, 'To eat something!', 'Use this function to eat anything from our menu!', '/eat <food>')
bot_function('menu', None, 'To get our menu card!','Use this function to get our menu card, for the food available!', '/menu')


# print(bot_function.list_of_commands)