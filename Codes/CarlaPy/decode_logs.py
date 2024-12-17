import os
import utils

def main():
    try:
        # TODO: Change THIS LINE TO YOUR OWN DIRECTORY, WHICH SHOULD BE AN ABSOLUTE PATH!
        dir_log = '/home/alex/Documents/autoSceneGenProj/CarlaPy/scenarios/'
        client = utils.create_carla_client()
        # Iterate over the log files in the directory
        for filename in os.listdir(dir_log):
            if filename.endswith('.recorded'):
                file_path = os.path.join(dir_log, filename)
                try:
                    # Save the result into a file with the same name as the log file
                    result = client.show_recorder_file_info(file_path, True)
                    result_file_path = os.path.join(dir_log, f"{os.path.splitext(filename)[0]}_decoded.txt")
                    with open(result_file_path, 'w') as result_file:
                        result_file.write(result)
                except Exception as e:
                    print(f"Error processing file {filename}: {e}")
    except Exception as error:
        import traceback
        traceback.print_exc()
    finally:
        print("Finished!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('\ndone.')
