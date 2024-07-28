import os
import cv2

def calculate_video_length(folder_path, selected_videos=None):
    """
    Calculate the total length of all videos in a folder.

    Args:
        folder_path (str): Path to the folder containing videos.
        selected_videos (list): List of video filenames to include in the calculation.

    Returns:
        float: Total length of all videos in seconds.
    """
    total_length = 0
    for filename in os.listdir(folder_path):
        if filename.endswith((".mkv", ".mp4", ".avi", ".mov")):
            if selected_videos is None or filename in selected_videos:
                video_path = os.path.join(folder_path, filename)
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print(f"Error: Could not open video file {filename}. Skipping.")
                    continue
                fps = cap.get(cv2.CAP_PROP_FPS)
                frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                length = frame_count / fps if fps > 0 else 0
                total_length += length
                cap.release()
    return total_length

def format_output(total_length):
    """
    Format the output in various formats.

    Args:
        total_length (float): Total length of all videos in seconds.

    Returns:
        dict: Formatted output in various formats.
    """
    output = {}
    output["seconds"] = total_length
    output["day_hr_min_sec"] = f"{int(total_length // 86400)} days, {int((total_length % 86400) // 3600)} hours, {int((total_length % 3600) // 60)} minutes, {int(total_length % 60)} seconds"
    output["minutes"] = total_length / 60
    output["hours"] = total_length / 3600
    output["days"] = total_length / 86400
    return output

def main():
    folder_path = input("Enter the folder path: ").strip()
    if not os.path.isdir(folder_path):
        print("Error: The provided folder path does not exist.")
        return

    video_files = [f for f in os.listdir(folder_path) if f.endswith((".mkv", ".mp4", ".avi", ".mov"))]
    if not video_files:
        print("Error: No supported video files found in the provided folder.")
        return

    print("Select an option:")
    print("1. Calculate total length of all videos in the folder")
    print("2. Select specific videos to calculate their total length")

    while True:
        option = input("Enter your choice (1/2): ").strip()
        if option == "1":
            total_length = calculate_video_length(folder_path)
            output = format_output(total_length)
            print("Total video length:")
            print(f"  * Seconds: {output['seconds']:.2f}")
            print(f"  * Day, Hour, Minute, Second: {output['day_hr_min_sec']}")
            print(f"  * Minutes: {output['minutes']:.2f}")
            print(f"  * Hours: {output['hours']:.2f}")
            print(f"  * Days: {output['days']:.2f}")
            break
        elif option == "2":
            print("Select videos to include in the calculation:")
            for i, video in enumerate(video_files):
                print(f"{i+1}. {video}")
            while True:
                selected_videos_input = input("Enter the numbers of the videos to include (separated by spaces), or a range (e.g., 1-5), or a combination of both (e.g., 1 2 3-5): ").strip()
                try:
                    parts = selected_videos_input.split()
                    selected_videos = []
                    for part in parts:
                        if '-' in part:
                            start, end = map(int, part.split('-'))
                            selected_videos.extend([video_files[i-1] for i in range(start, end+1)])
                        else:
                            selected_videos.append(video_files[int(part)-1])
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")
            total_length = calculate_video_length(folder_path, selected_videos)
            output = format_output(total_length)
            print("Total video length:")
            print(f"  * Seconds: {output['seconds']:.2f}")
            print(f"  * Day, Hour, Minute, Second: {output['day_hr_min_sec']}")
            print(f"  * Minutes: {output['minutes']:.2f}")
            print(f"  * Hours: {output['hours']:.2f}")
            print(f"  * Days: {output['days']:.2f}")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
