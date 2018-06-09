from User.user_data import User, Item


class table:
    def __init__(self):
        self.users = []
        self.test_id = {} #test_id['user_id'] = 'test_id'
        self.test_user_id = []

    def add_test(self, test_file):
        fi = open(test_file, 'r')
        while True:
            line = fi.readline()
            if not line:
                break
            line = line.split('\t')
            if not int(line[0]) in self.test_id:
                self.test_id[int(line[0])] = []
                self.test_user_id.append(int(line[0]))
            self.test_id[int(line[0])].append(int(line[1]))

    def add_user(self, input_file_name):
        fi = open(input_file_name, 'r')
        items = []
        rank_sum = 0
        now_id = 1
        while True:
            line = fi.readline()  # line: user_id, item_id, rating, timestamp
            if not line:
                break
            line = line.split('\t')
            line[3] = line[3][:len(line[3]) - 2]
            if int(line[0]) > now_id:
                this_user = User(now_id, items, rank_sum / len(items))
                self.users.append(this_user) # (user_id -1) is user list index
                items = []
                rank_sum = 0
                now_id += 1
            this_item = Item(int(line[1]), int(line[2]), int(line[3]))
            items.append(this_item)
            rank_sum += int(line[2])

    def test_fill(self, output_file):
        fo = open(output_file, 'w')
        test_ids = len(self.test_id)
        for i in self.test_user_id:
            test_idx = self.test_id[i]
            user_obj = self.users[i - 1]
            for j in test_idx:
                answer = user_obj.rank_mean
                sim_sum = 0
                predict = 0
                for k in self.users:
                    if k is user_obj:
                        continue
                    item = k.has_item(j)
                    if item is not None:
                        temp = user_obj.similarity(k)
                        temp2 = item.rank - k.rank_mean
                        sim_sum += temp
                        predict += temp*temp2

                if sim_sum > 0:
                    answer += predict/sim_sum
                answer = round(answer)
                if answer < 1:
                    answer = 1
                elif answer > 5:
                    answer = 5
                line = str(user_obj.user_id) + '\t' + str(j) + '\t' + str(answer) + '\n'
                #print(line)
                fo.write(line)
