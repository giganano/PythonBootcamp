
import numbers 


class body: 

	def __init__(self, name, mass): 
		self.name = name 
		self.mass = mass 

	@property 
	def name(self): 
		r""" 
		Type : str 

		The name of the star 
		""" 
		return self._name 

	@name.setter 
	def name(self, value): 
		if isinstance(value, str): 
			self._name = value 
		else: 
			raise TypeError("Attribute 'name' must be a string. Got: %s" % (
				type(value))) 

	@property 
	def mass(self): 
		r""" 
		Type : float 

		The mass of the star in solar masses 
		""" 
		return self._mass 

	@mass.setter 
	def mass(self, value): 
		if isinstance(value, numbers.Number): 
			self._mass = float(value) 
		else: 
			raise TypeError("Attribute 'mass' must be a real number. Got: %s" % (
				type(value))) 


class star(body): 
	pass 


class satellite(body): 

	def __init__(self, name, mass, semimajor_axis, eccentricity = 0): 
		super().__init__(name, mass) 
		self.semimajor_axis = semimajor_axis 
		self.eccentricity = eccentricity 

	@property 
	def semimajor_axis(self): 
		r""" 
		Type : float 

		The semimajor axis of the satellite's orbit in AU
		""" 
		return self._semimajor_axis 

	@semimajor_axis.setter 
	def semimajor_axis(self, value): 
		if isinstance(value, numbers.Number): 
			if value > 0: 
				self._semimajor_axis = value 
			else: 
				raise ValueError("""Attribute 'semimajor_axis' must be \
positive. Got: %f""" % (value)) 
		else: 
			raise TypeError("""Attribute 'semimajor_axis' must be a real \
number. Got: %s""" % (type(value))) 

	@property 
	def eccentricity(self): 
		r""" 
		Type : float 

		The eccentricity of the satellite's orbit 
		""" 
		return self._eccentricity 

	@eccentricity.setter 
	def eccentricity(self, value): 
		if isinstance(value, numbers.Number): 
			if 0 <= value <= 1: 
				self._eccentricity = value 
			else: 
				raise ValueError("""Attribute 'eccentricity' must be between 
0 and 1. Got: %f""" % (value)) 
		else: 
			raise TypeError("""Attribute 'eccentricity' must be a real \
number. Got: %s""" % (type(value))) 


class planet(satellite): 
	pass 


class moon(satellite): 
	pass 


class asteroid(satellite): 
	pass 


class comet(satellite): 
	pass 


class planetary_system: 

	def __init__(self, planet, moons): 
		self.planet = planet 
		self.moons = moons 

	@property 
	def planet(self): 
		r""" 
		Type : planet 

		The central planet 
		""" 
		return self._planet 

	@planet.setter 
	def planet(self, value): 
		if isinstance(value, planet): 
			self._planet = value 
		else: 
			raise TypeError("""Attribute 'planet' must be of type planet. \
Got: %s""" % (type(value))) 

	@property 
	def moons(self): 
		r""" 
		Type : list 

		A list of moon objects which orbit the planet 
		""" 
		return self._moons 

	@moons.setter 
	def moons(self, value): 
		if isinstance(value, list): 
			if all([isinstance(i, moon) for i in value]): 
				self._moons = value[:] 
			else: 
				raise TypeError("All moons must be of type moon.") 
		else: 
			raise TypeError("""Attribute 'moons' must be of type list. \
Got: %s""" % (type(value))) 


class solar_system: 

	def __init__(self, star, planets, asteroids, comets): 
		self.star = star 
		self.planets = planets 
		self.asteroids = asteroids 
		self.comets = comets 

	@property 
	def star(self): 
		r""" 
		Type : star 

		The central star of the solar system. 
		""" 
		return self._star 

	@star.setter 
	def star(self, value): 
		if isinstance(value, star): 
			self._star = value 
		else: 
			raise TypeError("Attribute 'star' must be of type star. Got: %s" % (
				type(value))) 

	@property 
	def planets(self): 
		r""" 
		Type : list 

		A list of planetary_system objects which orbit the central star. 
		""" 
		return self._planets 

	@planets.setter 
	def planets(self, value): 
		if isinstance(value, list): 
			if all([isinstance(i, planetary_system) for i in value]): 
				self._planets = value 
			else: 
				raise TypeError("All planets must be of type planetary_system.") 
		else: 
			raise TypeError("""Attribute 'planets' must be of type list. \
Got: %s""" % (type(value))) 

	@property 
	def asteroids(self): 
		r""" 
		Type : list 

		A list of asteroid objects which orbit the central star. 
		""" 
		return self._asteroids 

	@asteroids.setter 
	def asteroids(self, value): 
		if isinstance(value, list): 
			if all([isinstance(i, asteroid) for i in value]): 
				self._asteroids = value 
			else: 
				raise TypeError("All asteroids must be of type asteroid.") 
		else: 
			raise TypeError("""Attribute 'asteroids' must be of type list. \
Got: %s""" % (type(value))) 

	@property 
	def comets(self): 
		r""" 
		Type : list 

		A list of the comet objects which orbit the central star. 
		""" 
		return self._comets 

	@comets.setter 
	def comets(self, value): 
		if isinstance(value, list): 
			if all([isinstance(i, comet) for i in value]): 
				self._comets = value 
			else: 
				raise TypeError("All comets must be of type comet.") 
		else: 
			raise TypeError("""Attribute 'comets' must be of type comet. \
Got: %s""" % (type(value))) 

