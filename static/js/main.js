/**
 * main.js — Client-side search & filter for Google Cloud Summit 2026
 */

(function () {
  "use strict";

  /* -------------------------------------------------------
     Live search + category filter
     ------------------------------------------------------- */
  const searchInput  = document.getElementById("search-input");
  const searchClear  = document.getElementById("search-clear");
  const filterBtns   = document.querySelectorAll(".pill");
  const talksGrid    = document.getElementById("talks-grid");
  const noResults    = document.getElementById("no-results");
  const resultsCount = document.getElementById("results-count");

  // Also filter the timeline
  const timelineItems = document.querySelectorAll(".timeline-talk");

  let activeCategory = "";
  let searchQuery    = "";
  let debounceTimer  = null;

  function debounce(fn, delay) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(fn, delay);
  }

  function normalise(str) {
    return (str || "").toLowerCase().trim();
  }

  function applyFilters() {
    if (!talksGrid) return;

    const cards = talksGrid.querySelectorAll(".talk-card");
    let visible = 0;

    cards.forEach((card) => {
      const catMatch =
        !activeCategory || card.dataset.category === String(activeCategory);

      let textMatch = true;
      if (searchQuery) {
        const title    = normalise(card.querySelector(".talk-title")?.textContent);
        const desc     = normalise(card.querySelector(".talk-desc")?.textContent);
        const speakers = normalise(card.querySelector(".talk-speakers")?.textContent);
        textMatch = title.includes(searchQuery) || desc.includes(searchQuery) || speakers.includes(searchQuery);
      }

      if (catMatch && textMatch) {
        card.classList.remove("hidden");
        card.classList.remove("animating");
        // Trigger reflow to restart animation
        void card.offsetWidth;
        card.classList.add("animating");
        visible++;
      } else {
        card.classList.add("hidden");
        card.classList.remove("animating");
      }
    });

    // Update results count
    if (resultsCount) {
      if (searchQuery || activeCategory) {
        resultsCount.textContent = `${visible} talk${visible !== 1 ? "s" : ""} found`;
      } else {
        resultsCount.textContent = "";
      }
    }

    // No results message
    if (noResults) {
      noResults.hidden = visible > 0;
    }

    // Also filter the timeline schedule
    filterTimeline();
  }

  function filterTimeline() {
    timelineItems.forEach((item) => {
      const catMatch =
        !activeCategory || item.dataset.category === String(activeCategory);

      let textMatch = true;
      if (searchQuery) {
        const title    = normalise(item.querySelector(".card-title")?.textContent);
        const desc     = normalise(item.querySelector(".card-desc")?.textContent);
        const speakers = normalise(item.querySelector(".card-speakers")?.textContent);
        textMatch = title.includes(searchQuery) || desc.includes(searchQuery) || speakers.includes(searchQuery);
      }

      item.style.opacity = catMatch && textMatch ? "1" : "0.25";
    });
  }

  // Search input handler
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      searchQuery = normalise(searchInput.value);
      if (searchClear) searchClear.hidden = searchQuery === "";
      debounce(applyFilters, 200);
    });
  }

  // Clear search
  if (searchClear) {
    searchClear.addEventListener("click", () => {
      if (searchInput) searchInput.value = "";
      searchQuery = "";
      searchClear.hidden = true;
      applyFilters();
      searchInput?.focus();
    });
  }

  // Category filter pills
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("pill-active"));
      btn.classList.add("pill-active");
      activeCategory = btn.dataset.cat || "";
      applyFilters();
    });
  });

  /* -------------------------------------------------------
     Smooth nav highlight on scroll
     ------------------------------------------------------- */
  const navLinks = document.querySelectorAll(".nav-link");
  const sections = document.querySelectorAll("section[id]");

  function updateActiveNav() {
    let current = "";
    sections.forEach((sec) => {
      const top = sec.getBoundingClientRect().top;
      if (top <= 120) current = sec.id;
    });
    navLinks.forEach((link) => {
      const href = link.getAttribute("href") || "";
      link.style.color = href.includes(current) && current
        ? "var(--text-primary)"
        : "";
    });
  }

  window.addEventListener("scroll", updateActiveNav, { passive: true });

  /* -------------------------------------------------------
     Intersection Observer — fade-in on scroll
     ------------------------------------------------------- */
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.style.opacity = "1";
          e.target.style.transform = "translateY(0)";
          observer.unobserve(e.target);
        }
      });
    },
    { threshold: 0.08 }
  );

  // Animate stat items
  document.querySelectorAll(".stat-item").forEach((el, i) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = `opacity 0.5s ease ${i * 0.1}s, transform 0.5s ease ${i * 0.1}s`;
    observer.observe(el);
  });

  // Animate speaker cards
  document.querySelectorAll(".speaker-card").forEach((el, i) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(24px)";
    el.style.transition = `opacity 0.45s ease ${(i % 5) * 0.07}s, transform 0.45s ease ${(i % 5) * 0.07}s`;
    observer.observe(el);
  });

  // Animate talk cards (grid section)
  document.querySelectorAll(".talk-card").forEach((el, i) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(24px)";
    el.style.transition = `opacity 0.45s ease ${(i % 4) * 0.07}s, transform 0.45s ease ${(i % 4) * 0.07}s, border-color 0.22s, box-shadow 0.22s, background 0.22s`;
    observer.observe(el);
  });

  /* -------------------------------------------------------
     Keyboard shortcut — press '/' to focus search
     ------------------------------------------------------- */
  document.addEventListener("keydown", (e) => {
    if (e.key === "/" && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput?.focus();
      // Scroll into view
      searchInput?.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    if (e.key === "Escape" && document.activeElement === searchInput) {
      searchInput.blur();
    }
  });

})();
