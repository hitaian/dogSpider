class config():

    url = 'http://w2.aqu1024.club/pw/'


    def getType(self):

        # 新片速递
        movieType = {
            '最新合集': self.url + 'thread.php?fid=3',
            '亚洲无码': self.url + 'thread.php?fid=5',
            '日本骑兵': self.url + 'thread.php?fid=22',
            '欧美新片': self.url + 'thread.php?fid=7',
            '三级写真': self.url + 'thread.php?fid=18',
            '怪蜀黍区': self.url + 'thread.php?fid=81',
            '小毛驴区': self.url + 'thread.php?fid=79',
            '魔王专版': self.url + 'thread.php?fid=37',
            '灣搭专版': self.url + 'thread.php?fid=30',
            '最新快播': self.url + 'thread.php?fid=75',
            '唯美写真': self.url + 'thread.php?fid=14',
            '网友自拍': self.url + 'thread.php?fid=15',
            '露出激情': self.url + 'thread.php?fid=16',
            '偷窥原创': self.url + 'thread.php?fid=18',
            '成人小说': self.url + 'thread.php?fid=17'
        }
        return  movieType