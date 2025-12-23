scatter3(DataFinal,"log_ReactionRate","log_Temp","log_Density",'filled','ColorVariable','log_40Ca')
hold on
stem3(DataFinal,"log_ReactionRate","log_Temp","log_Density","Color","b")
colorbar
xlabel('Reaction Rate')
ylabel('Temperature(GK)')
zlabel('Density (g/cm)')
colormap turbo
xlim([-5,5])
ylim([-1,.5])
zlim([-.25,5])