import numpy as np
import matplotlib.pyplot as plt


# PlotMaker class to create function plots
class PlotMaker:
    def __init__(self, x_range=(-2 * np.pi, 2 * np.pi), num_points=1000):
        self.x = np.linspace(x_range[0], x_range[1], num_points)

    # Method to plot sine function
    def plot_sine(self):
        y = np.sin(self.x)
        plt.plot(self.x, y, label="sin(x)")
        plt.title('Sine Function')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Method to plot cosine function
    def plot_cosine(self):
        y = np.cos(self.x)
        plt.plot(self.x, y, label="cos(x)")
        plt.title('Cosine Function')
        plt.xlabel('x')
        plt.ylabel('cos(x)')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Method to plot tangent function
    def plot_tangent(self):
        y = np.tan(self.x)
        plt.plot(self.x, y, label="tan(x)")
        plt.title('Tangent Function')
        plt.xlabel('x')
        plt.ylabel('tan(x)')
        plt.ylim(-10, 10)  # Limit y-range to avoid tangent asymptotes
        plt.legend()
        plt.grid(True)
        plt.show()


# Main program
def main():
    plot_maker = PlotMaker()

    while True:
        print("Choose a plot option:")
        print("1. Plot Sine Function")
        print("2. Plot Cosine Function")
        print("3. Plot Tangent Function")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            plot_maker.plot_sine()
        elif choice == '2':
            plot_maker.plot_cosine()
        elif choice == '3':
            plot_maker.plot_tangent()
        elif choice == '4':
            print("Exiting the plot maker.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
