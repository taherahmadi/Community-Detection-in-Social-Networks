import csv


def read_file(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list


def write_file(file_name, partition_dictionary):
    with open(file_name, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['node_number', 'cluster_id'])
        for i in range(1, len(partition_dictionary) + 1):
            csv_writer.writerow([i, partition_dictionary[i] + 1])


def write_induced_graph(file_name, edges):
    with open(file_name, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['cluster_id', 'cluster_id', 'total_weight'])
        for item in edges:
            csv_writer.writerow([item[0] + 1, item[1] + 1, item[2]])


def write_number_of_nodes(file_name, node_array):
    with open(file_name, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['cluster_id', 'number_of_nodes'])
        i = 1
        for item in node_array:
            csv_writer.writerow([i, item])
            i += 1