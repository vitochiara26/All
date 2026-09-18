const playlists = [
    [
        {
            trackId: "trk101",
            artist: "Velvet Comet",
            title: "Crimson Afterglow",
            votes: 5,
            bpm: 122
        },
        {
            trackId: "trk102",
            artist: "Neon Harbor",
            title: "Static Horizon",
            votes: 2,
            bpm: 108
        },
        {
            trackId: "trk103",
            artist: "Lunar Arcade",
            title: "Midnight Frequency",
            votes: 4,
            bpm: 128
        }
    ],
    [
        {
            trackId: "trk201",
            artist: "Solar Echo",
            title: "Glass Skyline",
            votes: 3,
            bpm: 115
        },
        {
            trackId: "trk202",
            artist: "Velvet Comet",
            title: "Satellite Hearts",
            votes: 6,
            bpm: 124
        }
    ]
];

function flattenPlaylists(playlists) {
    if (!Array.isArray(playlists)) {
        return [];
    }
    const copyPlaylists = JSON.parse(JSON.stringify(playlists));
    const flatArr = [];
    for (let i = 0; i < copyPlaylists.length; i++) {
        for (let j = 0; j < copyPlaylists[i].length; j++) {
            copyPlaylists[i][j].source = [i, j];
            flatArr.push(copyPlaylists[i][j]);
        }
    }
    return flatArr;
}

const flatPlaylists = flattenPlaylists(playlists);

function scoreTracks(flatPlaylists) {
    const copyPlaylists = JSON.parse(JSON.stringify(flatPlaylists));
    const scoreArr = [];
    for (let i = 0; i < copyPlaylists.length; i++) {
        copyPlaylists[i].score = copyPlaylists[i].votes * 10 - Math.abs(copyPlaylists[i].bpm - 120);
        scoreArr.push(copyPlaylists[i]);
    }
    return scoreArr;
}

const scoredPlaylists = scoreTracks(flatPlaylists);

function dedupeTracks(scoredPlaylists) {
    const uniqueTracksIds = [];
    const uniqueTracks = [];
    for (let i = 0; i < scoredPlaylists.length; i++) {
        if (!uniqueTracksIds.includes(scoredPlaylists[i].trackId)) {
            uniqueTracksIds.push(scoredPlaylists[i].trackId);
            uniqueTracks.push(scoredPlaylists[i]);
        }
    }
    return uniqueTracks;
}

const dedupedPlaylists = dedupeTracks(scoredPlaylists);

function enforceArtistQuota(dedupedPlaylists, maxPerArtist) {
    const enforcedPlaylist = []
    const artistQuots = {};
    for (let i = 0; i < dedupedPlaylists.length; i++) {
        if (!artistQuots.hasOwnProperty(dedupedPlaylists[i].artist)) {
            const key = dedupedPlaylists[i].artist;
            artistQuots[key] = 0;
            enforcedPlaylist.push(dedupedPlaylists[i]);
            artistQuots[dedupedPlaylists[i].artist] += 1;
        } else {
            if (artistQuots[dedupedPlaylists[i].artist] < maxPerArtist) {
                enforcedPlaylist.push(dedupedPlaylists[i]);
                artistQuots[dedupedPlaylists[i].artist] += 1;
            }
        }
    }
    return enforcedPlaylist;
}

const enforcedPlaylists = enforceArtistQuota(dedupedPlaylists, 1);

function buildSchedule(enforcedPlaylists) {
    const schedule = [];
    for (let i = 0; i < enforcedPlaylists.length; i++) {
        schedule.push({ slot: i + 1, trackId: enforcedPlaylists[i].trackId });
    }
    return schedule
}

const playlistsSchedule = buildSchedule(enforcedPlaylists);

function remixPlaylist(playlists, maxPerArtist) {
    const flatPlaylist = flattenPlaylists(playlists);
    const scoredPlaylists = scoreTracks(flatPlaylist);
    const dedupedTracks = dedupeTracks(scoredPlaylists);
    const enforcedArtists = enforceArtistQuota(dedupedTracks, maxPerArtist);
    const schedule = buildSchedule(enforcedArtists);
    return schedule;
}

remixPlaylist(playlists, 1)