fimport unittest
from modulplaner import Modulplaner 



class ModulplanerTest(unittest.TestCase):
    def setUp(self):
        self.mp = Modulplaner(max:_credits_per_semester=10)
        self.mp.add_modul("WI101", 6)                        
        self.mp.add_modul("WT201", 5, {"WI101"})
        
        
    def test_plan_ok_and_credits(self):
        self.mp.plan_modul(1, "WT101", status="bestanden")
        self.assertEqual(self.mp.semester_credits(1), 6)    
        self.assertEqual(self.mp.total_credits(), 6)     
                    
                        
    def test_prerequisite_blocks(self):
        with self.assertRaises(ValueError):
            self.mp.plan_modul(1, "WI201")         
                                                                
                                                                                            
    def test_credit_limit(self):          
        self.mp.add_modul("WI102", 5)
        self.mp.plan_modul(1, "WI101")
        with self.assertRaises(ValueError):
            self.mp.plan_modul(1, "WI102")



if __name__ == "__main__":
    unittest.main()
