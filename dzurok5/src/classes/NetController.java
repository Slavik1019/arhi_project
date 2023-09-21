package classes;

import interfaces.iCommonInterface;

class NetController implements iCommonInterface {
	private RoadRepository roadRepo;
	private CameraRepository cameraRepo;
	private CurrentTrafficRepository trafficRepo;

	public NetController(RoadRepository roadRepo, CameraRepository cameraRepo, CurrentTrafficRepository trafficRepo) {
		this.roadRepo = roadRepo;
		this.cameraRepo = cameraRepo;
		this.trafficRepo = trafficRepo;
	}

	@Override
	public void methodFromInterface() {
		System.out.println("NetController");
	}
	
}