class RepetitionCounter:
    def __init__(self):
        self.start_position = None  # Starting Y position of the object
        self.lowest_position = None  # Lowest Y position seen in the current rep
        self.highest_position = None  # Highest Y position seen in the current rep
        self.reps_completed = 0  # Total number of reps completed

    def update(self, position):
        """
        Update the counter with the current position of the object.
        :param position: The current Y position of the object.
        """
        if self.start_position is None:
            # If it's the first position we're tracking, initialize start position
            self.start_position = position

        # Update highest and lowest positions
        if self.lowest_position is None or position < self.lowest_position:
            self.lowest_position = position
        if self.highest_position is None or position > self.highest_position:
            self.highest_position = position

        # Check if a rep is completed
        if self.is_rep_completed(position):
            self.reps_completed += 1
            # Reset for the next rep
            self.lowest_position = None
            self.highest_position = None

    def is_rep_completed(self, position):
        """
        Determine if a repetition is completed based on the current position.
        :param position: The current Y position of the object.
        :return: True if a rep is completed, False otherwise.
        """
        # Define the logic to determine if a rep is completed
        # This is a simplified example; you'll need to adjust it based on the exercise
        # and the range of motion
        threshold = 10  # Define a threshold for considering when a rep is completed
        if self.highest_position and self.lowest_position:
            # Check if the object returned close to the starting position
            return abs(position - self.start_position) < threshold
        return False

    def get_reps(self):
        """
        Get the total number of repetitions completed.
        :return: The total number of reps completed.
        """
        return self.reps_completed
