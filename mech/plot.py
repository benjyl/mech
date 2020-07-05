from matplotlib import pyplot as plt


def plot_trackpoints(trackpoints):
   
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)
    ax1.set(xlabel="Distance (m)", ylabel="Absolute radius of curvature (m)")
    ax2.set(xlabel="Distance (m)", ylabel="Velocity (m/s)")
    ax3.set(xlabel="Distance (m)", ylabel="Acceleration (m/s^2)")
    ax4.set(xlabel="Distance (m)", ylabel="Normal force (N)")
    ax5.set(xlabel="Distance (m)", ylabel="Lateral force (N)")
    ax6.set(xlabel="Distance (m)", ylabel="Longitudinal force (N)")

    curvature_cutoff = 1000
    
    distances = [point.distance for point in trackpoints]

    ax1.plot(distances, [min(abs(point.curvature_radius), curvature_cutoff) for point in trackpoints])
    ax2.plot(distances, [point.velocity for point in trackpoints])
    ax3.plot(distances, [point.acceleration for point in trackpoints])
    ax4.plot(distances, [point.normal_force for point in trackpoints])
    ax5.plot(distances, [point.lateral_force for point in trackpoints])
    ax6.plot(distances, [point.longitudinal_force for point in trackpoints])

    ax1.hlines(
        y=curvature_cutoff,
        xmin=0,
        xmax=trackpoints[-1].distance,
        color="r",
        linestyle="dashed",
    )

    plt.show()
