# <?php

# class StopWatch
# {
#     /**
#      * @var float
#      */
#     private $startTime;

#     /**
#      * @var float
#      */
#     private $stopTime;

#     /**
#      * @var array|float[]
#      */
#     private $times = [];

#     public function Start()
#     {
#         $this->startTime = microtime(true);
#     }

#     /**
#      * @return StopWatch
#      */
#     public static function StartNew()
#     {
#         $sw = new StopWatch();
#         $sw->Start();
#         return $sw;
#     }

#     public function Stop()
#     {
#         $this->stopTime = microtime(true);
#     }

#     /**
#      * @param string $label
#      */
#     public function Record($label)
#     {
#         $this->times[$label] = microtime(true);
#     }

#     /**
#      * @param string $label
#      * @return float
#      */
#     public function GetRecordSeconds($label)
#     {
#         return $this->times[$label] - $this->startTime;
#     }

#     /**
#      * @param string $label1
#      * @param string $label2
#      * @return float
#      */
#     public function TimeBetween($label1, $label2)
#     {
#         return $this->times[$label1] - $this->times[$label2];
#     }

#     /**
#      * @return float
#      */
#     public function GetTotalSeconds()
#     {
#         return $this->stopTime - $this->startTime;
#     }
# }

from fastapi import FastAPI
import time

app = FastAPI()

class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
        self.times = {}

    def start(self):
        self.start_time = time.time()

    @classmethod
    def start_new(cls):
        sw = cls()
        sw.start()
        return sw

    def stop(self):
        self.stop_time = time.time()

    def record(self, label):
        self.times[label] = time.time()

    def get_record_seconds(self, label):
        return self.times[label] - self.start_time

    def time_between(self, label1, label2):
        return self.times[label1] - self.times[label2]

    def get_total_seconds(self):
        return self.stop_time - self.start_time

@app.post("/stopwatch/")
def stopwatch():
    stopwatch = StopWatch()
    stopwatch.start()
    
    # Perform some tasks here and record time intervals
    stopwatch.record("Task 1")
    time.sleep(1)
    
    stopwatch.record("Task 2")
    time.sleep(0.5)
    
    stopwatch.stop()
    
    result = {
        "total_seconds": stopwatch.get_total_seconds(),
        "time_between_tasks": stopwatch.time_between("Task 2", "Task 1"),
    }
    return result

