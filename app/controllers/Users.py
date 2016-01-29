from system.core.controller import *
from geopy.geocoders import Nominatim

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.load_model('Match')

    def index(self):
        return self.load_view('index.html')

    def process_login(self):
        user_info = {
        'clientID': request.form['clientID'],
        'accessToken': request.form['accessToken'],
        'email': request.form['email'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
        }

        status = self.models['User'].process_login(user_info)
        session['id'] = status['user']['id']
        return redirect('/process_home')

    def success(self):
        return self.load_view('success.html')

    def home(self):
        return self.load_view('home.html')

    def profile(self):
        about = self.models['User'].get_aboutMe_by_id(session['id'])
        return self.load_view('profile.html', about = about)

    def friends_page(self):
        return redirect('/home')

    def communicate(self):
        # self.models['Match'].find_is_matched(
        return self.load_view('messages.html')

    def messages_page(self):
        return redirect('/communicate')

    def register_page(self):
        return self.load_view('register.html')

    def logout(self):
        session.clear()
        return redirect('/')


    def about_me(self):
        latitude = request.form['lat']
        longitude = request.form['long']
        my_info = {
            'content' : request.form['content'],
            'user' : session['id'],
            'gender' : request.form['gender'],
            'latitude' : latitude,
            'longitude' : longitude,
            'age' : request.form['age']
        }
        self.models['User'].add_user_info(my_info)
        # geolocator
        geolocator = Nominatim()
        location = geolocator.reverse(request.form['lat'] + ',' + request.form['long'])
        print(location.address)
        print my_info
        # end geolocator
        return redirect('/profile')

    # def get_info(self, id):

    #     return redirect('/profile')


    def about(self):
        return self.load_view('about.html')

    def contact(self):
        return self.load_view('contact.html')

    def team(self):
        return self.load_view('team.html')
