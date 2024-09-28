import unittest
class crime:
    def __init__(self,crime_id,crime_type,description,location):
        self.crime_id = crime_id
        self.crime_type = crime_type
        self.description = description
        self.location = location
class CrimeMap:
    def __init__(self):
        self.crimes = {}
    def add_crime(self,crime):
        if crime.crime_id in self.crimes:
            raise ValueError("Crime ID already there.")
        self.crimes[crime.crime_id]=crime
    def read_crime(self,crime_id):
        return self.crimes.get(crime_id)
    def delete_crime(self,crime_id):
        if crime_id in self.crimes:
            del self.crimes[crime_id]
    def map_crime_location(self):
        print("Crime Locations:")
        for crime in self.crimes.values():
            print(f"{crime.crime_id}:{crime.location}")
    def analyze_crime_patterns(self):
        patterns = {}
        for crime in self.crimes.values():
            if crime.crime_type in patterns:
                patterns[crime.crime_type]+=1
            else:
                patterns[crime.crime_type]=1
        return patterns
class TestCrimeMap(unittest.TestCase):
    def setUp(self):
        self.map=CrimeMap()
        self.map.add_crime(crime('001','Theft','Stolen bike',(10,10)))
        self.map.add_crime(crime('002','Assault','Assault in park',(20,20)))
    def test_add_crime_existing_id(self):
        with self.assertRaises(ValueError):
            self.map.add_crime(crime('001','Burglary','store burglary',(15,15)))
    def test_delete_crime(self):
        self.map.delete_crime('001')
        self.assertIsNone(self.map.read_crime('001'))
    def test_analyze_patterns(self):
        patterns =self.map.analyze_crime_patterns()
        self.assertEqual(patterns['Theft'],1)
        self.assertEqual(patterns['Assault'],1)
        
if __name__=="__main__":
    unittest.main()
   

    
    
