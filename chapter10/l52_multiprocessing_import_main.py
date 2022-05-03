import multiprocessing
import l53_multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=l53_multiprocessing_import_worker.worker, )
    jobs.append(p)
    p.start()
    