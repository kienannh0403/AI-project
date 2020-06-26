import random as rnd 
from prettytable import PrettyTable # thư viện dùng để kẻ bảng
# from Schedule import Schedule
class Data:

	ROOMS = [["B401",25],["B402",60],["B404",50],["E401",35] ,["C401",50], ["D401",35] ]
	MEETINGTIMES = [["Ca 1-2", "6:50 - 9:15","Thu 2"],
					["Ca 2-2", "9:25 - 11:50","Thu 2"],
					["Ca 3-2", "12:30 - 14:55","Thu 2"],
					["Ca 4-2", "15:05 - 17:25","Thu 2"],
					["Ca 1-3", "6:50 - 9:15","Thu 3"],
					["Ca 2-3", "9:25 - 11:50","Thu 3"],
					["Ca 3-3", "12:30 - 14:55","Thu 3"],
					["Ca 4-3", "15:05 - 17:25","Thu 3"],
					["Ca 1-4", "6:50 - 9:15","Thu 4"],
					["Ca 2-4", "9:25 - 11:50","Thu 4"],
					["Ca 3-4", "12:30 - 14:55","Thu 4"],
					["Ca 4-4", "15:05 - 17:25","Thu 4"],
					["Ca 1-5", "6:50 - 9:15","Thu 5"],
					["Ca 2-5", "9:25 - 11:50","Thu 5"],
					["Ca 3-5", "12:30 - 14:55","Thu 5"],
					["Ca 4-5", "15:05 - 17:25","Thu 5"],
					["Ca 1-6", "6:50 - 9:15","Thu 6"],
					["Ca 2-6", "9:25 - 11:50","Thu 6"],
					["Ca 3-6", "12:30 - 14:55","Thu 6"],
					["Ca 4-6", "15:05 - 17:25","Thu 6"],
					["Ca 1-7", "6:50 - 9:15","Thu 7"],
					["Ca 2-7", "9:25 - 11:50","Thu 7"],
					["Ca 3-7", "12:30 - 14:55","Thu 7"],
					["Ca 4-7", "15:05 - 17:25","Thu 7"]]
	INTRUCTORS = [["GV0","Thay H"],
				["GV1","Thay A"],
				["GV2","Thay B"],
				["GV3","Thay C"],
				["GV4","Co A"],
				["GV5","Co B"]]

	def __init__(self):
		self._rooms = []
		self._meetingtimes = []
		self._intructors = []
		#tạo danh sách phòng học
		for i in range(0, len(self.ROOMS)):
			self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
		#tạo dánh sách giờ học
		for i in range(0, len(self.MEETINGTIMES)):
			self._meetingtimes.append(MeetingTime(self.MEETINGTIMES[i][0], self.MEETINGTIMES[i][1],self.MEETINGTIMES[i][2]))
		# tạo danh sách giảng viên
		for  i in range(0,len(self.INTRUCTORS)):
			self._intructors.append(Intructor(self.INTRUCTORS[i][0], self.INTRUCTORS[i][1]))

		intrucs_cour1 = [self._intructors[0], self._intructors[3]]
		intrucs_cour2 = [self._intructors[1], self._intructors[2]]
		intrucs_cour3 = [self._intructors[2], self._intructors[3]]
		intrucs_cour4 = [self._intructors[3], self._intructors[4]]
		intrucs_cour5 = [self._intructors[5], self._intructors[4]]
		intrucs_cour6 = [self._intructors[2]]
		#tạo danh sách môn học 
		course1 = Course("MH0", "Co So Du Lieu" , intrucs_cour1, 25)
		course2 = Course("MH1", "Cau Truc Du Lieu" ,intrucs_cour2 , 35)
		course3 = Course("MH2", "Nhap Mon Mang May Tinh" ,intrucs_cour3 , 25)
		course4 = Course("MH3", "Nhap Mon Tri Tue Nhan Tao" ,intrucs_cour4 , 45)
		course5 = Course("MH4", "Nhap Mon Hoc May" ,intrucs_cour5 , 45)
		course6 = Course("MH6", "Cong Nghe Phan Mem" ,intrucs_cour6 , 30)
		self._courses = [course1,course2,course3,course4,course5,course6]
		#tạo danh sách ban phụ trách môn học
		dept1 = Department("KHMT",[course5,course4])
		dept2 = Department("LTUD",[course1,course2,course6])
		dept3 = Department("MTH",[course3])
		self._depts = [dept1,dept2,dept3]
		self._numofclass = 0
		for i in range(len(self._depts)):
			self._numofclass += len(self._depts[i].get_courses())

	def get_rooms_data(self): #hàm gọi danh sách phòng
		return self._rooms

	def get_intructors_data(self): # hàm gọi danh sách giảng viên
		return self._intructors

	def get_courses_data(self):# hàm gọi danh sách môn học
		return self._courses

	def get_depts_data(self):# hàm gọi danh sách khoa phụ trách
		return self._depts

	def get_meetingtimes_data(self):# hàm gọi danh sách ca học
		return self._meetingtimes		

class Schedule: #Thời khóa biểu
	def __init__(self): # hàm khởi tạo dữ kiện để tạo thời khóa biểu
		self._data = data
		self._classes = []
		self._numconflict = 0
		self._fitness = -1
		self._isfitchanged = True
		self._classnum = 0

	def get_classes_schedule(self): # hàm gọi các lớp học trong TKB
		self._isfitchanged = True
		return self._classes

	def get_numconflict(self): # hàm gọi số lượng xung đột
		return self._numconflict

	def get_fitness(self): #tính số cân bằng
		if (self._isfitchanged == True ):
			self._fitness = self.cal_fitness()
			self._isfitchanged = False
		return self._fitness

	def cal_fitness(self): # hàm tính toán độ cân bằng TKB
		classes = self.get_classes_schedule()
		for i in range(len(classes)): # nếu số lượng học sinh lớn hơn số lượng chỗ ngồi thì tăng số xung đột lên 1
			if(classes[i].get_room().get_numofseat() < classes[i].get_course().get_numofstudent()):
				self._numconflict += 1
			for j in range(len(classes)):
				if (j >= i):
					if(classes[i].get_meetingtime() == classes[j].get_meetingtime() and classes[i].get_id_class() != classes[j].get_id_class()):
						if( classes[i].get_room() == classes[j].get_room()): #2 lớp học có cùng 1 phòng học
							self._numconflict += 1
						if( classes[i].get_intructor() == classes[j].get_intructor()):# 2 lớp học có cùng 1 giáo viên
							self._numconflict += 1
		return 1 / ((1.0*self._numconflict + 1))

	def initialize_schedule(self):# hàm khởi tạo thời khóa biểu
		depts = self._data.get_depts_data()
		for i in range(len(depts)):
			courses = depts[i].get_courses()
			for j in range(len(courses)): 
				#tạo lớp học mới
				newclass = Class(self._classnum, depts[i], courses[j])
				self._classnum += 1
				newclass.set_meetingtime(data.get_meetingtimes_data()[rnd.randrange(len(data.get_meetingtimes_data()))])
				newclass.set_room(data.get_rooms_data()[rnd.randrange(len(data.get_rooms_data()))])
				# if (len(courses[j].get_intructor_course()) == 1):
				# 	newclass.set_intructor(data.get_intructor_())
				# else:
				newclass.set_intructor(data.get_intructors_data()[rnd.randrange(len(courses[j].get_intructor_course()))])
				self._classes.append(newclass)
		return self

	def __str__(self): #hàm toString 
		returnValue = " "
		for i in range(len(self._classes) -1):
			returnValue += str(self._classes[i]) +"|| "
		returnValue += str(self._classes[len(self._classes)-1])
		return returnValue

class GeneticAlgo: # thuật toán di truyền
	def evolve (self,population):# hàm tiến hóa
		return self._mutate_population(self._crossover_population(population))
	
	def _crossover_population(self,population):
		crossover_pop = Population(0)
		for i in range(Num_elite_schedule):
			crossover_pop.get_schedules().append(population.get_schedules()[i])
		i = Num_elite_schedule
		while  i < POPULATION_Size:
			schedule1 =	self._select_population(population).get_schedules()[0]
			schedule2 = self._select_population(population).get_schedules()[0]
			crossover_pop.get_schedules().append(self._crossover_schedule(schedule1,schedule2))
			i += 1
		return crossover_pop

	def _mutate_population(self,population):
		for i in range(Num_elite_schedule, POPULATION_Size):
			self._mutate_schedule(population.get_schedules()[i])
		return population

	def _crossover_schedule(self, schedule1, schedule2):
		crossoverschedule = Schedule().initialize_schedule()
		for i in range(len(crossoverschedule.get_classes_schedule())):
			if (rnd.random() > 0.5):
				crossoverschedule.get_classes_schedule()[i] = schedule1.get_classes_schedule()[i]
			else:
				crossoverschedule.get_classes_schedule()[i] = schedule2.get_classes_schedule()[i]
		return crossoverschedule

	def _mutate_schedule(self, mutateschedule):
		schedule = Schedule()
		schedule.initialize_schedule()
		for i in range(len(mutateschedule.get_classes_schedule())):
			if(Mutation_rate > rnd.random()):
				mutateschedule.get_classes_schedule()[i] = schedule.get_classes_schedule()[i]
		return mutateschedule

	def _select_population(self,population):
		tournament_population = Population(0)
		i = 0
		while i < tournament_size:
			tournament_population.get_schedules().append(population.get_schedules()[rnd.randrange(0, POPULATION_Size)])
			i += 1
		tournament_population.get_schedules().sort(key = lambda x : x.get_fitness(), reverse = True)
		return tournament_population

class Population:
	def __init__(self, size):
		self._size = size
		self._data = data
		self._schedules = []
		for i in range(size):
			self._schedules.append(Schedule().initialize_schedule())

	def get_schedules(self):
		return self._schedules

class Course: #Môn học
	def  __init__(self,idnumber, name, intructors, numofstudent): #hàm khởi tạo 1 môn học mới
		self._number = idnumber
		self._name = name
		self._intructors = intructors
		self._numofstudent= numofstudent

	def get_idnumber(self): #hàm gọi ID môn học 
		return self._number
	def get_name_cour(self): #hàm gọi tên môn hoc
		return self._name
	def get_intructor_course(self):# hàm gọi giảng viên phụ trách giảng dạy
		return self._intructors 
	def get_numofstudent(self): #hàm gọi số lượng SV học môn này
		return self._numofstudent
	def __str__(self):
		return self._name 

class Intructor: #Giảng viên
	def __init__(self, id, name): #hàm khởi tạo giảng viên
		self._id = id 
		self._name = name

	def get_id_intruc(self): #hàm gọi mã GV
		return self._id
	def get_name_intrc(self): #hàm gọi tên giảng viên
		return self._name
	def __str__(self): #hàm in ra 1 dãy 
		return self._name

class Department: # Khoa phụ trách
	def __init__(self, name, courses): # hàm khởi tạo khoa mới
		self._name = name
		self._courses = courses

	def  get_name_dept(self):# hàm gọi tên khoa 
		return self._name
	def get_courses(self):# hàm gọi các môn khoa phụ trách
		return self._courses

class Room: #phòng học
	def __init__(self, idnumber, numofseat):# hàm khai báo phòng 
		self._number = idnumber
		self._numofseat = numofseat

	def get_id_room(self): #hàm gọi id phòng
		return self._number
	def get_numofseat(self): #hàm gọi số lượng chỗ ngồi
		return self._numofseat

class MeetingTime: #Giờ học
	def __init__(self,id, time,day): # khai báo giờ học mới
		self._id_meeting = id
		self._time=time
		self._day=day

	def get_id_meetingtimes(self): # hàm gọi phòng học
		return self._id_meeting

	def get_time(self): # hàm gọi thời gian học (ca học)
		return self._time

	def get_day(self):
		return self._day

class Class: #lớp học 
	def __init__(self, id, dept, course): # hàm khởi tạo lớp học mới (VD: lớp 125A2 - phòng A1)
		self._id_class = id
		self._dept = dept
		self._course = course
		self._intructor = None
		self._meetingtime = None
		self._room = None
	
	def get_id_class(self): # hàm gọi id lớp
		return self._id_class
	def get_dept(self): #hàm gọi khoa phụ trách
		return self._dept
	def get_course(self): # hàm gọi môn học lớp mà lớp học
		return self._course
	def get_intructor(self): #hàm gọi giảng viên phụ trách
		return self._intructor
	def set_intructor(self,intructor): # set 1 giảng viên phụ trách môn học
		self._intructor = intructor
	def get_meetingtime(self): #hàm gọi ca học 
		return self._meetingtime
	def set_meetingtime(self, meetingTime): # set ca học cho môn học
		self._meetingtime = meetingTime
	def get_room(self): # hàm gọi phòng học
		return self._room
	def set_room(self, room): #hàm set phòng học
		self._room = room
	def __str__(self): #hàm toString
		return str(self._dept.get_name_dept())+","+str(self._course.get_idnumber()) + "," + \
				str(self._room.get_id_room()) + "," + str(self._intructor.get_id_intruc()) + "," + str(self._meetingtime.get_id_meetingtimes())

class Display: # hàm hiển thị kết quả
	
	# def print_data(self): #hàm hiển thị dữ liệu
	# 	print("DATA:")
	# 	self.print_department()
	# 	self.print_course()
	# 	self.print_intructor()
	# 	self.print_room()
	# 	self.print_meetingtime()
	
	# def print_department(self): #hàm ỉn a dư liệu khoa
	# 	print("DEPARTMENT:")
	# 	avadept = PrettyTable()
	# 	depts = data.get_depts_data()
	# 	avadept.field_names = ['Department', 'Courses']
	# 	for i in range(len(depts)):
	# 		courses = depts.__getitem__(i).get_courses()
	# 		tempStr = "["
	# 		for j in range(len(courses) - 1):
	# 			tempStr += courses[i].__str__() + ","
	# 		tempStr += courses[len(courses)-1].__str__() + "]"
	# 		avadept.add_row([depts.__getitem__(i).get_name_dept(), tempStr])
	# 	print(avadept)

	# def print_course(self): # hàm ỉn a dữ liệu môn học
	# 	print("COURSE:")
	# 	avacourse = PrettyTable()
	# 	avacourse.field_names = ['ID', 'Course', 'Max # of student', 'Intructor']
	# 	courses = data.get_courses_data()
	# 	for i in range(len(courses)):
	# 		intructors = courses[i].get_intructor_course()
	# 		tempStr= " "
	# 		for j in range(0,len(intructors) -1 ):
	# 			tempStr += intructors[j].__str__()+ ","
	# 		tempStr += intructors[len(intructors) - 1].__str__()
	# 		avacourse.add_row([courses[i].get_idnumber(), courses[i].get_name_cour(), courses[i].get_numofstudent(), tempStr])
	# 	print(avacourse)

	# def print_intructor(self):# hàm in ra dư liệu giảng viên
	# 	print("INTRUCTOR:")
	# 	avaintructor = PrettyTable()
	# 	intructors = data.get_intructors_data()
	# 	avaintructor.field_names = ['ID', 'INTRUCTOR']
	# 	for i in range(len(intructors)):
	# 		avaintructor.add_row([intructors[i].get_id_intruc(), intructors[i].get_name_intrc()])
	# 	print(avaintructor)

	# def print_room(self):# hàm in ra dữ liệu phòng học
	# 	print("ROOM:")
	# 	avaroom  = PrettyTable()
	# 	avaroom.field_names = ['Room #', 'Max capacity']
	# 	rooms = data.get_rooms_data()
	# 	for i in range(len(rooms)):
	# 		avaroom.add_row([str(rooms[i].get_id_room()), str(rooms[i].get_numofseat())])
	# 	print(avaroom)

	# def print_meetingtime(self):# hàm in ra dữ kiệu ca học
	# 	print("MEETING TIME:")
	# 	avameetingtime = PrettyTable()
	# 	avameetingtime.field_names = ['id','MeetingTime']
	# 	meetingtimes = data.get_meetingtimes_data()
	# 	for i in range(len(meetingtimes)):
	# 		avameetingtime.add_row([meetingtimes[i].get_id_meetingtimes(), meetingtimes[i].get_time()])
	# 	print(avameetingtime)

	def print_gene(self,population): 
		
		table1 = PrettyTable()
		table1.field_names = ['schedule:','fitness','conflict:','classes(dept, course, class, room, intructor)']
		schedules = population.get_schedules()
		for i in range (len(schedules)):
			table1.add_row([str(i+1),
							round(schedules[i].get_fitness(),3), 
							schedules[i].get_numconflict(),
							schedules[i]])
		print(table1)

	def print_schedule_table(self,schedule): # hàm in ra TKB
		print("SCHEDULE: ")
		table = PrettyTable()
		classes = schedule.get_classes_schedule()
		table.field_names = ['Class #', 'Dept ','Course(ID Course and max student)','Room(Number of Capacity)','Intructor', 'Studying Shift']
		for i in range(len(classes)):
			table.add_row([str(i+1), 
							classes[i].get_dept().get_name_dept(),
							classes[i].get_course().get_name_cour() + "(" +classes[i].get_course().get_idnumber() + ","+ str(classes[i].get_course().get_numofstudent()) +")", 
							classes[i].get_room().get_id_room() + "(" + str(classes[i].get_room().get_numofseat())+")" ,
							classes[i].get_intructor().get_name_intrc() + "(" + str(classes[i].get_intructor().get_id_intruc())+ ")" ,
							classes[i].get_meetingtime().get_time() + "(" + str(classes[i].get_meetingtime().get_id_meetingtimes()) +","+ str(classes[i].get_meetingtime().get_day()) +")"])
		print(table)


POPULATION_Size = 5
Num_elite_schedule = 1
tournament_size = 3
Mutation_rate = 0.1
data = Data()
display = Display()
# display.print_data()
geneNumber = 0
print("\n Genetion :" + str(geneNumber))
population = Population(POPULATION_Size)
population.get_schedules().sort(key = lambda x : x.get_fitness(), reverse = True)
display.print_gene(population)
display.print_schedule_table(population.get_schedules()[0])
genetic = GeneticAlgo()
print(population.get_schedules()[0].get_fitness())
if (population.get_schedules()[0].get_fitness() == 1):
	geneNumber += 1
	print("\n Genetion #" + str(geneNumber))
	population = genetic.evolve(population)
	population.get_schedules().sort(key = lambda x: x.get_fitness(), reverse = True )
	display.print_gene(population)
	display.print_schedule_table(population.get_schedules()[0])


