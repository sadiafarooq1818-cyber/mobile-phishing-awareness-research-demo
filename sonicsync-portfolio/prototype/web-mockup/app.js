const tabs = document.querySelectorAll('.tab');
const screens = document.querySelectorAll('.screen');
const roomModal = document.getElementById('roomModal');
const roomCode = document.getElementById('roomCode');
const roomLabel = document.getElementById('roomLabel');
const deviceCount = document.getElementById('deviceCount');
const latencyValue = document.getElementById('latencyValue');
const deviceList = document.getElementById('deviceList');
const toast = document.getElementById('toast');
const playPause = document.getElementById('playPause');
const syncStatus = document.getElementById('syncStatus');
const syncPulse = document.getElementById('syncPulse');

let roomActive = false;
let playing = false;
let clientsAdded = false;

function openScreen(id) {
  tabs.forEach((tab) => tab.classList.toggle('active', tab.dataset.screen === id));
  screens.forEach((screen) => screen.classList.toggle('active', screen.id === id));
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.remove('hidden');
  window.setTimeout(() => toast.classList.add('hidden'), 2200);
}

function createRoom() {
  const number = Math.floor(100 + Math.random() * 900);
  roomCode.textContent = `SYNC-${number}`;
  roomLabel.textContent = `Room ${roomCode.textContent} · Host`;
  roomActive = true;
  latencyValue.textContent = '42 ms';
  syncStatus.textContent = 'Host ready';
  syncPulse.classList.add('live');
  roomModal.classList.remove('hidden');
}

tabs.forEach((tab) => tab.addEventListener('click', () => openScreen(tab.dataset.screen)));

document.getElementById('createRoom').addEventListener('click', createRoom);
document.getElementById('joinRoom').addEventListener('click', () => {
  roomActive = true;
  roomLabel.textContent = 'Room SYNC-531 · Client';
  latencyValue.textContent = '58 ms';
  syncStatus.textContent = 'Connected to host';
  syncPulse.classList.add('live');
  showToast('Joined demonstration room SYNC-531');
  openScreen('devices');
});

document.getElementById('closeModal').addEventListener('click', () => {
  roomModal.classList.add('hidden');
  openScreen('devices');
});

document.getElementById('scanDevices').addEventListener('click', () => {
  if (!roomActive) {
    showToast('Create or join a room before scanning.');
    return;
  }
  if (clientsAdded) {
    showToast('Device list refreshed.');
    return;
  }
  const scanningCard = document.createElement('article');
  scanningCard.className = 'device-card';
  scanningCard.innerHTML = '<div class="device-avatar">…</div><div><strong>Searching local network</strong><span>Wi-Fi discovery in progress</span></div><span class="status searching">Scanning</span>';
  deviceList.appendChild(scanningCard);

  window.setTimeout(() => {
    scanningCard.remove();
    [
      ['A', 'Android Phone A', 'Client · Living room', '35 ms'],
      ['B', 'Android Phone B', 'Client · Study room', '49 ms']
    ].forEach(([letter, name, description, latency]) => {
      const card = document.createElement('article');
      card.className = 'device-card';
      card.innerHTML = `<div class="device-avatar">${letter}</div><div><strong>${name}</strong><span>${description} · ${latency}</span></div><span class="status connected">Ready</span>`;
      deviceList.appendChild(card);
    });
    clientsAdded = true;
    deviceCount.textContent = '3';
    latencyValue.textContent = '49 ms';
    syncStatus.textContent = '3 devices synchronized';
    showToast('Two nearby devices connected.');
  }, 1100);
});

playPause.addEventListener('click', () => {
  if (!roomActive) {
    showToast('Create or join a room first.');
    openScreen('home');
    return;
  }
  playing = !playing;
  playPause.textContent = playing ? 'Ⅱ' : '▶';
  playPause.setAttribute('aria-label', playing ? 'Pause' : 'Play');
  syncStatus.textContent = playing ? `${deviceCount.textContent} devices playing together` : 'Playback paused on all devices';
  syncPulse.classList.toggle('live', playing || roomActive);
  showToast(playing ? 'Synchronized playback started.' : 'Playback paused for every device.');
});

document.getElementById('settingsButton').addEventListener('click', () => showToast('Settings mockup: buffer size, device name and network mode.'));
