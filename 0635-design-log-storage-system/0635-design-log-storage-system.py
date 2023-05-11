class LogSystem:

    def __init__(self):
        self.logs = []
        self.lst_map = {'Year': '01/01/%y', 'Month': '%m/01/%y', 'Day': '%m/%d/%y', 'Hour': '%m/%d/%y %H:00:00', 'Minute': '%m/%d/%y %H:%M:00', 'Second': '%m/%d/%y %H:%M:%S' }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append([id, timestamp])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        lst_id = self.lst_map[granularity]
        
        from datetime import datetime
        start_dt = datetime.strptime(start,'%Y:%m:%d:%H:%M:%S')
        end_dt = datetime.strptime(end,'%Y:%m:%d:%H:%M:%S')
        s_dt = start_dt.strftime(lst_id)
        e_dt = end_dt.strftime(lst_id)

        new = []
        for idx, time in self.logs:
            dt = datetime.strptime(time,'%Y:%m:%d:%H:%M:%S')
            t_dt = dt.strftime(lst_id)
            if datetime.strptime(s_dt, lst_id) <= datetime.strptime(t_dt, lst_id) <= datetime.strptime(e_dt, lst_id) and idx not in new:
                new.append(idx)
        return new

    # Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)