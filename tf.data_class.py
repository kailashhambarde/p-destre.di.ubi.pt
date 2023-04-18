import os
import os.path as osp
import glob

class Pdestre:
    root = "/home/socialab/Downloads/pedestrian/"
    test_out_path = "/home/socialab/Downloads/pedestrian/"
    split_path = "/home/socialab/Downloads/pedestrian/Splits/"
    
    def __init__(self, root='', split_id=0):
        self.root = osp.abspath(osp.expanduser(root))
        self.split_path = osp.join(self.root, self.split_path)
        self.test_out_path = osp.join(self.root, self.test_out_path)
        print(self.root)
        
        max_splits = 5
        if split_id > (max_splits):
            #-1 becuase we have 0 to 4 splits
            raise ValueError("split_id exceeds range, received {}, but expected between 0 and {}".format(split_id, (max_splits) - 1))

        # declare some variables
        train_name = self.split_path + 'Train_' + str(split_id) + '.txt'
        train_dirs = self._read_seqmaps(train_name)
        query_name = self.split_path + 'Query_' + str(split_id) + '.txt'
        query_dirs = self._read_seqmaps(query_name)
        gallery_name = self.split_path + 'Gallery_' + str(split_id) + '.txt'
        test_dirs = self._read_seqmaps(gallery_name)

        train_dir2pid = list()
        train, num_train_tracklets, num_train_pids, num_imgs_train, train_pid_list,train_dir2pid = self._process_data(train_dirs, train_dir2pid, 0)

        test_dir2pid = list()
        query, num_query_tracklets, num_query_pids, num_imgs_query, test_pid_list,train_dir2pid = self._process_data(query_dirs, test_dir2pid, 0)

        gallery, num_gallery_tracklets, num_gallery_pids, num_imgs_gallery, gal_pid_list,train_dir2pid = self._process_data(test_dirs, test_pid_list, 0)

        self.train = train
        self.query = query
        self.gallery = gallery
        self.num_train_tracklets = num_train_tracklets
        self.num_train_pids = num_train_pids
        self.num_imgs_train = num_imgs_train
        self.num_query_tracklets = num_query_tracklets
        self.num_query_pids = num_query_pids
        self.num_imgs_query = num_imgs_query
        self.num_gallery_tracklets = num_gallery_tracklets
        self.num_gallery_pids = num_gallery_pids
        self.num_imgs_gallery = num_imgs_gallery
        self.train_dir2pid = train_dir2pid

    def _read_seqmaps(self, fname):
        """
        seqmap: list the sequence name to be evaluated
        """
        assert os.path.exists(fname), 'File %s not exists!' % fname
        with open(fname, 'r') as fid:
            lines = [line.strip() for line in fid.readlines()]
            seqnames = lines
        return seqnames

    def _process_data(self, dirnames, dir2pid, test_flag):
        tracklets = []
        num_imgs_per_tracklet = []
        PID_LIST = list()
        train_dir2pid = list()

        for dirname in dirnames:
            pid_path = osp.join(self.root, dirname)
            P_ID = os.path.basename(pid_path)[:-2]
            pid_dirnames = os.listdir(pid_path)

            for pidfolder in pid_dirnames:
                if int(pidfolder) > 0:
                    pid_folder = P_ID + '-' + pidfolder
                    pid_int = pid_folder.split('-')
                    pid = "".join(pid_int)

                    if pid not in dir2pid:
                        dir2pid.append(pid)
                        train_dir2pid.append(pid)
                    if test_flag == 1 and pid not in PID_LIST:
                        PID_LIST.append(pid)

        if test_flag == 1:
            test_dirname2pid = {dirname: i for i, dirname in enumerate(PID_LIST)}
        dirname2pid = {dirname: i for i, dirname in enumerate(dir2pid)}

        nums_pid = 0
        for dirname in dirnames:
            pid_path = osp.join(self.root, dirname)
            Sequence_id = os.path.basename(pid_path)[-1]
            P_ID = os.path.basename(pid_path)[:-2]
            pid_dirnames = os.listdir(pid_path)

            for pidfolder in pid_dirnames:
                if int(pidfolder) > 0:
                    person_dir = osp.join(pid_path, pidfolder)
                    img_list = glob.glob(osp.join(person_dir, '*.jpg'))
                    img_names_list = [imag for imag in img_list if os.path.getsize(imag) > 0]

                    for img_name in img_names_list:
                        pid_folder = P_ID + '-' + pidfolder
                        pid_int = pid_folder.split('-')
                        pid = "".join(pid_int)
                        pid = dirname2pid[pid]

                        tracklets.append((img_name, pid, Sequence_id))
                        num_imgs_per_tracklet.append(1)
                        nums_pid += 1

        num_tracklets = len(tracklets)

        if test_flag == 1:
            num_pids = len(test_dirname2pid)
        else:
            num_pids = len(dirname2pid)

        pid_dirlt = dir2pid
        num_train_cams = 1

        return tracklets, num_tracklets, num_pids, num_imgs_per_tracklet, pid_dirlt, train_dir2pid


